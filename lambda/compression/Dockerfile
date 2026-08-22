FROM public.ecr.aws/lambda/python:3.13

COPY requirements.txt ${LAMBDA_TASK_ROOT}/
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY handler.py ${LAMBDA_TASK_ROOT}/
COPY image_processor.py ${LAMBDA_TASK_ROOT}/
COPY s3_service.py ${LAMBDA_TASK_ROOT}/

CMD ["handler.handler"]