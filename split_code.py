import argparse
from pathlib import Path


def chunk_text(text: str, size: int, overlap: int = 0):
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    if overlap < 0 or overlap >= size:
        raise ValueError("Overlap must be non-negative and smaller than size")

    start = 0
    text_len = len(text)
    while start < text_len:
        end = min(start + size, text_len)
        yield text[start:end]
        start = end - overlap


def main():
    parser = argparse.ArgumentParser(description="Split text file into roughly equal-sized chunks.")
    parser.add_argument("input", type=Path, help="Path to input text file")
    parser.add_argument("--size", type=int, default=3800, help="Target chunk size in characters (default: 3800)")
    parser.add_argument("--overlap", type=int, default=0, help="Optional number of overlapping characters between chunks")
    parser.add_argument("--output-dir", type=Path, help="Directory to store chunk files; prints to stdout if omitted")

    args = parser.parse_args()

    text = args.input.read_text(encoding="utf-8")
    chunks = list(chunk_text(text, args.size, args.overlap))

    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        for idx, chunk in enumerate(chunks, start=1):
            suffix = args.input.suffix or ".txt"
            out_path = args.output_dir / f"{args.input.stem}_part{idx:02d}{suffix}"
            out_path.write_text(chunk, encoding="utf-8")
            print(out_path)
    else:
        for idx, chunk in enumerate(chunks, start=1):
            header = f"===== Chunk {idx}/{len(chunks)} ({len(chunk)} chars) ====="
            print(header)
            print(chunk)
            print()


if __name__ == "__main__":
    main()
