import argparse

from lib.face import Face


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, default='sample/michael-dam-mEZ3PoFGs_k-unsplash.jpg',
                        required=False, help='Image path')
    parser.add_argument('--video', type=bool, default=False,
                        required=False, help='Realtime Video input')
    parser.add_argument('--face', type=bool, default=False,
                        required=False, help='Detect Face')
    parser.add_argument('--eye', type=bool, default=False,
                        required=False, help='Detect Eye')

    args = parser.parse_args()
    process_list = []
    if args.face:
        process_list.append('face')
    if args.eye:
        process_list.append('eye')

    detection = Face()
    if args.video:
        detection.video(process_list)
    else:
        detection.load(args.image)
        detection.process(process_list)
        detection.show()
