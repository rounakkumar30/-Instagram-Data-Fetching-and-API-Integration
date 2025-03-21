

# **📸 Instagram Data Fetching & API Integration**

## **🚀 Overview**
This project fetches the latest post from the **BBC News Instagram page**, retrieving the **caption** and **image**. It uses the **Instagram Graph API** or **web scraping** if API access is unavailable.

---

## **📌 Features**
✅ Fetches the latest post's **caption** and **image URL**  
✅ Displays the data in a **Django web page**  
✅ Implements **error handling** and **logging**  
✅ Allows changing the target Instagram username  

---

## **🛠️ Setup Instructions**

### **1️⃣ Create a Meta Developer App**
1. Go to [Meta for Developers](https://developers.facebook.com/) and create an app.
2. Select **"Business"** as the app type.
3. Add **Instagram Graph API** in the product section.
4. Connect an **Instagram Business Account** via [Meta Business Suite](https://business.facebook.com/).

### **2️⃣ Generate an Instagram Access Token**
1. Open [Graph API Explorer](https://developers.facebook.com/tools/explorer/).
2. Select your app and add the following permissions:
   - `instagram_basic`
   - `pages_show_list`
   - `instagram_manage_insights`
3. Click **Generate Access Token** and **Authorize** it.
4. Run the API request to get your **Instagram User ID**:

   ```sh
   https://graph.instagram.com/me?fields=id,username&access_token=ACCESS_TOKEN
   ```

### **3️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

### **4️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **5️⃣ Set Up Environment Variables**
Create a `.env` file in the project directory and add:

```
INSTAGRAM_ACCESS_TOKEN=your_access_token
INSTAGRAM_USER_ID=your_user_id
```

---

## **🖥️ Running the Project**
```sh
python manage.py runserver
```
Visit: **http://127.0.0.1:8000/**

---

## **🛠 API Endpoints**
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/instagram/latest-post/` | Fetch the latest Instagram post |

---

## **📌 Example Output**
The web page will display:
- The **caption** of the post
- The **image**
- A **link to the original post**

---

## **⚠️ Troubleshooting**
1. **Access Token Expired?**  
   - Generate a [long-lived token](https://developers.facebook.com/docs/facebook-login/access-tokens/refreshing) to avoid frequent expiration.
  
2. **No Posts Found?**  
   - Ensure your Instagram account is **Business/Creator** and linked to a **Facebook Page**.

---

## **📜 License**
This project is **MIT Licensed**.

