import theme_parks
from map_builder import build_map


def main():
    print("Fetching park data...")
    parks = theme_parks.fetch_all_parks()

    print("Building map...")
    fmap = build_map(parks, theme_parks)

    output_file = 'theme_parks_queue_times.html'
    fmap.save(output_file)
    print(f"Map saved to {output_file}. Open it in your browser.")


if __name__ == '__main__':
    main()
