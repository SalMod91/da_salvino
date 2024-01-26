from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField
from cloudinary.uploader import upload, destroy


class IngredientCategory(models.Model):
    """
    Represents a category for ingredients.

    Attributes:
    - name (CharField): The name of the ingredient category, with a maximum
      length of 20 characters.
    - order (IntegerField): The order in which this category should appear.
      A lower value indicates a higher priority for display.
    """
    name = models.CharField(max_length=20, unique=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ingredient Category"
        verbose_name_plural = "Ingredient Categories"
        ordering = ['order', 'name']


class Ingredient(models.Model):
    """
    Represents an ingredient used in pizza preparation.

    Attributes:
    - name (CharField): The name of the ingredient,
      unique and limited to 25 characters.
    - category (ForeignKey): A ForeignKey relationship to the
      IngredientCategory model.
      Indicates the category to which this ingredient belongs.
    - description (TextField): An optional description of the ingredient.
    - image (CloudinaryField): An optional image of the ingredient,
      stored and managed via Cloudinary.
      The image is stored in the 'ingredients' folder on Cloudinary.
    - created_at (DateTimeField): Date and time when the ingredient was
      created. This field is automatically set.
    - updated_at (DateTimeField): Date and time when the ingredient was last
      updated. This field is automatically updated.

    The save method is overridden to handle image uploads.
    If an image is provided, it is uploaded to Cloudinary and the URL is stored
    in the image field. If no image is provided, a default image URL is used.
    The delete method is also overridden to ensure that the associated
    image is deleted from Cloudinary when the Ingredient object is deleted.
    """
    name = models.CharField(max_length=25, unique=True)
    category = models.ForeignKey(
        IngredientCategory, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = CloudinaryField(
        'image', blank=True, null=True, folder='ingredients')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to handle image uploads.
        If an image file is present,it saves the ingredient without the image,
         uploads the image to Cloudinary to generate a public ID,
        and then saves the ingredient again with the updated image URL.
        This approach ensures that the image is stored with a consistent
        naming convention based on the ingredient's ID.
        If no image file is provided, it simply saves the model as is.
        """
        if hasattr(self.image, 'file'):  # Check if it's a file to upload
            temp_image = self.image
            self.image = None
            super(Ingredient, self).save(*args, **kwargs)
            # Generate the public_id based on the ingredient ID
            public_id = f'ingredient_image_{self.id}'

            # Upload the image with the correct public_id and overwrite
            # if it is the same public_id
            upload_options = {
                'public_id': public_id,
                'overwrite': True,
                'folder': 'ingredients'
            }
            uploaded_image = upload(temp_image, **upload_options)

            # Update the image field with the new public_url and save again
            self.image = uploaded_image['secure_url']
            super(Ingredient, self).save(*args, **kwargs)

        else:
            # If the image field is empty, execute this code
            if not self.image:
                # Sets the image to the default image stored on Cloudinary
                self.image = (
                    'https://res.cloudinary.com/dplsavizt/image/upload/'
                    'v1705999566/image/default_image.jpg'
                )

            # Save the model
            super(Ingredient, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Overrides the default delete method to handle the deletion of the
        associated image from Cloudinary. When an ingredient is deleted,
        this method checks for an associated image. If found, it constructs
        the public_id of the image based on the ingredient's ID and the
        predefined folder path ('ingredients'). The Cloudinary API is then
        called to delete the image from cloud storage. Afterward, it
        proceeds to delete the Ingredient instance from the database.
        """

        if self.image:
            public_id = f'ingredients/ingredient_image_{self.id}'
            destroy(public_id)

        super(Ingredient, self).delete(*args, **kwargs)


class Pizza(models.Model):
    """
    Pizza model representing a pizza menu item.

    Attributes:
    - name (CharField): The name of the pizza
    - has_tomato (BooleanField): Indicates whether the pizza has tomato sauce
    - has_mozzarella (BooleanField): Indicates whether the pizza has mozzarella
    - ingredients (ManyToManyField): The ingredients included in the pizza
      Relates to the Ingredient model
    - image (CloudinaryField): An image of the pizza,
      stored and managed via Cloudinary
    """

    # Name of the pizza; max length 20 characters
    name = models.CharField(max_length=20, unique=True)

    # Boolean fields indicating whether the pizza has tomato and mozzarella
    has_tomato = models.BooleanField(default=False)
    has_mozzarella = models.BooleanField(default=False)

    # Many-to-many relationship with the Ingredient model
    # 'blank=True' allows the pizza to be saved without any ingredients
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    # Image field using Cloudinary for image hosting
    # 'blank=True, null=True' means the image is optional
    image = CloudinaryField('image', blank=True, null=True, folder='pizzas')

    def __str__(self):
        """
        Returns the name of the Pizza.
        """
        return self.name

    class Meta:
        """
        Meta options for the Pizza model.
        """
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"

    def save(self, *args, **kwargs):
        """
        Overrides the default save method for image uploads. If an image file
        is present, it saves the pizza without the image, uploads the image to
        Cloudinary to generate a public ID, then saves it again with the
        updated image URL. This ensures a consistent naming convention based on
        the pizza's ID. If no image file is provided, it saves the model as is.
        """

        if hasattr(self.image, 'file'):  # Check if it's a file to upload
            temp_image = self.image
            self.image = None
            super(Pizza, self).save(*args, **kwargs)
            # Generate the public_id based on the ingredient ID
            public_id = f'pizza_image_{self.id}'

            # Upload the image with the correct public_id
            # and overwrite if same public_id
            upload_options = {
                'public_id': public_id,
                'overwrite': True,
                'folder': 'pizzas'
            }
            uploaded_image = upload(temp_image, **upload_options)

            # Update the image field with the new public_url and save again
            self.image = uploaded_image['secure_url']
            super(Pizza, self).save(*args, **kwargs)

        else:
            # If the image field is empty, execute this code
            if not self.image:
                # Sets the image to the default image stored on Cloudinary
                self.image = (
                    'https://res.cloudinary.com/dplsavizt/image/upload/'
                    'v1705999566/image/default_image.jpg'
                )

            # Save the model
            super(Pizza, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Overrides the default delete method for Cloudinary image deletion.
        When a pizza is deleted, it checks for an associated image. If found,
        the public_id is based on the pizza's ID and 'pizzas' folder.
        The image is then deleted from Cloudinary before deleting the pizza
        instance from the database.
        """

        if self.image:
            public_id = f'pizzas/pizza_image_{self.id}'
            destroy(public_id)

        super(Pizza, self).delete(*args, **kwargs)
