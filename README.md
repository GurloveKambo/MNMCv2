# Mount Nelson Medical Centre — live HotDoc availability build

This GitHub Pages-ready static site shows next HotDoc availability against each GP.

## Live HotDoc availability
- Website reads `assets/hotdoc-availability.json`.
- GitHub Actions workflow `.github/workflows/refresh-hotdoc-availability.yml` refreshes it every 30 minutes.
- Manual refresh: Actions → Refresh HotDoc availability → Run workflow.

## Required GitHub settings
1. Upload all files to GitHub.
2. Settings → Actions → General → allow actions.
3. Workflow permissions → **Read and write permissions**.
4. Run the workflow once manually.

## Booking links
- HotDoc: https://www.hotdoc.com.au/medical-centres/mount-nelson-TAS-7007/mt-nelson-medical-centre/doctors
- HealthEngine: https://healthengine.com.au/medical-centre/tas/mount-nelson/mount-nelson-medical-centre/s15185
- Care Sync: https://nelson-care-sync.base44.app

## Note
HotDoc does not provide a guaranteed public static API from this listing. If HotDoc changes page markup or blocks automated access, the workflow preserves prior data and the website tells patients to open HotDoc for confirmed live times.
