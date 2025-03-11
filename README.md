

#### Automated Jira Ticket Creation via GitHub Webhooks and Flask API

This project automates the creation of Jira tickets using GitHub webhooks. When a comment containing `/jira` is added to a GitHub issue, 
the system triggers a Flask API to create a corresponding ticket in Jira.

---

### Features
- **GitHub Integration**: Listens for issue comments containing `/jira`.
- **Flask API**:Accept json payload from Github webHooks via request module. 
- **Jira API Interaction**: Creates tickets in Jira based on GitHub issue details.  
- **Hosting**: Deployed FlaskAPI on AWS EC2 for reliable performance.  

---

### **Tech Stack**
- **Backend**: Python, Flask  
- **APIs**: Jira API, GitHub Webhooks  
- **Hosting**: AWS EC2  (Flask API)

---

### **How It Works**
1. A comment with `/jira` is added to a GitHub issue.  
2. GitHub sends a webhook payload to the Flask API.  
3. The API processes the payload and creates a Jira ticket.  
4. The response is logged and returned for verification.  

---

### **Setup**
1. Clone the repository:  
   
   git clone https://github.com/your-username/your-repo.git
  
2. Install dependencies:  
   
   pip install -r requirements.txt
   
3. Configure GitHub webhooks and Jira API credentials.  
4. Deploy the Flask app on AWS EC2 or locally.
5. Edit inbound rule allowing 5000 port  

---

### **Useability**
- Add a comment with `/jira` to a GitHub issue.  
- A Jira ticket will be automatically created with the issue details.
- Reduces the Deveopler manual task.

---

### **Contributing**
Feel free to open issues or submit pull requests for improvements!  



