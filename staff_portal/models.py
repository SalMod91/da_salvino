from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField
from cloudinary.uploader import upload, destroy


class IngredientCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ingredient Category"
        verbose_name_plural = "Ingredient Categories"


class Ingredient(models.Model):
    name = models.CharField(max_length=25, unique=True)
    category = models.ForeignKey(IngredientCategory, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = CloudinaryField('image', blank=True, null=True, folder='ingredients')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to handle image uploads. If an image file is present,
        it saves the ingredient without the image, uploads the image to Cloudinary to
        generate a public ID, and then saves the ingredient again with the updated image URL.
        This approach ensures that the image is stored with a consistent naming convention
        based on the ingredient's ID. If no image
        file is provided, it simply saves the model as is.
        """
        if hasattr(self.image, 'file'):  # Check if it's a file to upload
            temp_image = self.image
            self.image = None
            super(Ingredient, self).save(*args, **kwargs)
            # Generate the public_id based on the ingredient ID
            public_id = f'ingredient_image_{self.id}'

            # Upload the image with the correct public_id and overwrite if same public_id
            upload_options = {'public_id': public_id, 'overwrite': True, 'folder': 'ingredients'}
            uploaded_image = upload(temp_image, **upload_options)

            # Update the image field with the new public_id and save again
            self.image = uploaded_image['public_id']
            self.image = uploaded_image['secure_url']
            super(Ingredient, self).save(*args, **kwargs)
        else:
            # If it's not a file, just save the model as is
            super(Ingredient, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Overrides the default delete method to handle the
        deletion of the associated image from Cloudinary.
        When an ingredient is deleted, this method checks if there is an associated image.
        If there is, it constructs the public_id of the image based on the ingredient's ID
        and the predefined folder path ('ingredients').
        It then calls the Cloudinary API to delete the image from the cloud storage.
        After deleting the image, it proceeds with deleting the Ingredient instance from the database.
        """

        if self.image:
            public_id = f'ingredients/ingredient_image_{self.id}'
            destroy(public_id)

        super(Ingredient, self).delete(*args, **kwargs)
