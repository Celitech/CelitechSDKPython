# TopUpEsimRequest

**Properties**

| Name             | Type  | Required | Description                                                                                                                                                                                                            |
| :--------------- | :---- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| iccid            | str   | ✅       | ID of the eSIM                                                                                                                                                                                                         |
| data_limit_in_gb | float | ✅       | Size of the package in GB. The available options are 0.5, 1, 2, 3, 5, 8, 20GB                                                                                                                                          |
| start_date       | str   | ✅       | Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.                                                                         |
| end_date         | str   | ✅       | End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.                                                                                                       |
| email            | str   | ❌       | Email address where the purchase confirmation email will be sent (excluding QR Code & activation steps).                                                                                                               |
| reference_id     | str   | ❌       | An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes.                                                                                      |
| email_brand      | str   | ❌       | Customize the email subject brand. The `emailBrand` parameter cannot exceed 25 characters in length and must contain only letters, numbers, and spaces. This feature is available to platforms with Diamond tier only. |
| start_time       | float | ❌       | Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months.                                                                |
| end_time         | float | ❌       | Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time.                                                                                                     |
