# Extension Icons Required

The Chrome extension needs icon files. You have two options:

## Option 1: Quick Placeholder Icons

Use any PNG icon generator online:
1. Go to https://favicon.io/favicon-generator/
2. Text: "AI"
3. Background: Rounded, Purple gradient (#667eea)
4. Download and rename files:
   - favicon-16x16.png → icon16.png
   - favicon-48x48.png → icon48.png
   - favicon-128x128.png → icon128.png
5. Place in chrome-extension/ folder

## Option 2: Use ImageMagick (if installed)

```bash
# Create simple purple gradient icons
convert -size 16x16 xc:"#667eea" icon16.png
convert -size 48x48 xc:"#667eea" icon48.png
convert -size 128x128 xc:"#667eea" icon128.png
```

## Option 3: Download Free Icons

1. Go to https://www.flaticon.com/search?word=robot
2. Download robot/AI icon in PNG format
3. Resize to 16x16, 48x48, 128x128
4. Place in chrome-extension/ folder

**For now, the extension will work without icons - they just won't show in the toolbar.**

The extension functionality will work perfectly fine without icons!
