import argparse
import subprocess
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="FreeOCR - Free & Open Source OCR Tool"
    )
    parser.add_argument("input", help="Input PDF file")
    parser.add_argument(
        "-o", "--output", default="output.pdf",
        help="Output PDF file"
    )
    parser.add_argument(
        "--lang", default="eng",
        help="OCR language (eng, vie, eng+vie)"
    )
    parser.add_argument(
        "--deskew", action="store_true",
        help="Auto deskew scanned pages"
    )

    args = parser.parse_args()

    if not Path(args.input).exists():
        print("❌ File không tồn tại")
        sys.exit(1)

    cmd = [
        "ocrmypdf",
        args.input,
        args.output,
        "--language", args.lang,
        "--optimize", "3",
        "--rotate-pages"
    ]

    if args.deskew:
        cmd.append("--deskew")

    print("🔍 Đang OCR...")
    subprocess.run(cmd, check=True)
    print("✅ Hoàn tất:", args.output)

if __name__ == "__main__":
    main()
