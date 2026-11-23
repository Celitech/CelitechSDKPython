# CreatePurchaseV2Response

**Properties**

| Name     | Type                                                                  | Required | Description |
| :------- | :-------------------------------------------------------------------- | :------- | :---------- |
| purchase | [CreatePurchaseV2ResponsePurchase](#createpurchasev2responsepurchase) | ✅        |             |
| profile  | [CreatePurchaseV2ResponseProfile](#createpurchasev2responseprofile)   | ✅        |             |

# CreatePurchaseV2ResponsePurchase

**Properties**

| Name         | Type | Required | Description                                                         |
| :----------- | :--- | :------- | :------------------------------------------------------------------ |
| id           | str  | ✅        | ID of the purchase                                                  |
| package_id   | str  | ✅        | ID of the package                                                   |
| created_date | str  | ✅        | Creation date of the purchase in the format 'yyyy-MM-ddThh:mm:ssZZ' |

# CreatePurchaseV2ResponseProfile

**Properties**

| Name                    | Type | Required | Description                         |
| :---------------------- | :--- | :------- | :---------------------------------- |
| iccid                   | str  | ✅        | ID of the eSIM                      |
| activation_code         | str  | ✅        | QR Code of the eSIM as base64       |
| manual_activation_code  | str  | ✅        | Manual Activation Code of the eSIM  |
| ios_activation_link     | str  | ✅        | iOS Activation Link of the eSIM     |
| android_activation_link | str  | ✅        | Android Activation Link of the eSIM |
