from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
import argparse
import os

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='Convert directory to file')
    parser.add_argument('dir', type=str, help='input directory')
    parser.add_argument('out', type=str, help='output file path')

    # 解析命令行参数
    args = parser.parse_args()

    # 验证输入的目录参数是否存在
    if not os.path.isdir(args.dir):
        print('Error: input directory does not exist')
        return

    documents = SimpleDirectoryReader(input_dir=args.dir,recursive=True).load_data()
    index = GPTSimpleVectorIndex.from_documents(documents)
    index.save_to_disk(args.out)

if __name__ == '__main__':
    main()
