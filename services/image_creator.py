from PIL import Image, ImageFont, ImageDraw


class ImageCreatorService:
    def __init__(self, base_image_path: str):
        self.name_font = ImageFont.truetype('./fonts/Montserrat-Bold.ttf', 40)
        self.job_font = ImageFont.truetype('./fonts/Montserrat-Bold.ttf', 26)
        self.contact_font = ImageFont.truetype('./fonts/OpenSans-Regular.ttf', 20)
        self.base_image_path = base_image_path

    def create_signatures(self, persons):
        for person in persons:
            self.create_signature(person)

    def create_signature(self, person):
        img = Image.open(self.base_image_path)
        draw = ImageDraw.Draw(img)

        # add name
        draw.text((30, 20), person.get_full_name(), font=self.name_font, fill=(0, 0, 0))

        # add job
        draw.text((30, 65), person.job, font=self.job_font, fill=(0, 128, 0))

        # add contact
        draw.text((55, 105), person.email, font=self.contact_font, fill=(0, 0, 0))
        draw.text((55, 130), person.get_tel(), font=self.contact_font, fill=(0, 0, 0))

        # Display edited image
        img.show()

        img.save(person.get_full_name() + ".png")
