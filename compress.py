from PIL import Image
import os

images_to_compress = {
    'logo.jpeg': {'max_size': 100, 'quality': 75}, # target size 100x100
    'image copy 5.png': {'max_size': 800, 'quality': 80, 'format': 'JPEG'} # target 800px width, convert to JPEG maybe?
}

for img_name, config in images_to_compress.items():
    if os.path.exists(img_name):
        try:
            img = Image.open(img_name)
            
            # Convert to RGB if necessary (for saving as JPEG)
            if img.mode in ('RGBA', 'P') and config.get('format') == 'JPEG':
                img = img.convert('RGB')
                
            # Resize
            max_size = config['max_size']
            img.thumbnail((max_size, max_size))
            
            # Save
            if config.get('format') == 'JPEG':
                out_name = img_name.replace('.png', '.jpeg')
                img.save(out_name, 'JPEG', quality=config['quality'])
                print(f"Compressed {img_name} to {out_name}")
                if out_name != img_name:
                    pass # Keep the old one just in case we need to update HTML
            else:
                img.save(img_name, quality=config['quality'])
                print(f"Compressed {img_name}")
                
        except Exception as e:
            print(f"Error compressing {img_name}: {e}")
