Build and deploy using AWS Toolkit for Jetbrains:
* Use these parameters below to deploy the application.
    * Temp Configuration:
  ```bash
  Environment=temp
  Origin=http://localhost:3000
  ```

Deployment steps:
* Build template:
  `sam build --use-container`
* Package:
  `sam package --template-file ~/aws_serverless_sample/.aws-sam/build/template.yaml --output-template-file ~/aws_serverless_sample/.aws-sam/build/packaged-template.yaml --s3-bucket ass-deployment`
* Deploy:
  `sam deploy --stack-name ass-temp --s3-bucket heka-deployment --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM --no-execute-changeset --parameter-overrides \"Environment\"=\"temp\" \"Origin\"=\"http://localhost:3000\"`
