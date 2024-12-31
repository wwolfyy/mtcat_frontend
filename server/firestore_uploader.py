import marimo

__generated_with = "0.10.7"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    from googleapiclient.discovery import build
    from google.oauth2.service_account import Credentials
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import firestore
    return Credentials, build, credentials, firebase_admin, firestore, pd


@app.cell
def _(Credentials, build, credentials, firebase_admin, firestore, pd):
    # Firebase Authentication
    cred = credentials.Certificate('path/to/your/serviceAccountKey.json')  # Replace with your service account key file
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # Google Sheets Authentication
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    creds = Credentials.from_service_account_file('path/to/your/credentials.json', scopes=scopes)
    service = build('sheets', 'v4', credentials=_creds)

    # Spreadsheet ID
    spreadsheet_id = 'your_spreadsheet_id'  # Replace with your spreadsheet ID

    # Get spreadsheet data
    sheet_range = 'Sheet1!A1:Z'  # Replace with your sheet name and range
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=sheet_range).execute()
    values = result.get('values', [])

    # Create Pandas DataFrame
    df = pd.DataFrame(values[1:], columns=values[0])  # Skip header row

    # Write to Firestore
    for index, row in df.iterrows():
        data = row.to_dict()
        db.collection('your_collection_name').document(str(index)).set(data)  # Replace with your collection name

    print("Data successfully written to Firestore!")
    return (
        cred,
        creds,
        data,
        db,
        df,
        index,
        result,
        row,
        scopes,
        service,
        sheet_range,
        spreadsheet_id,
        values,
    )


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
