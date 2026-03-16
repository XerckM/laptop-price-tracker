const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8000";

export type Offer = {
  id: number;
  price: string;
  currency: string;
  url: string;
  in_stock: boolean;
  retailer_name: string;
};

export type Product = {
  id: number;
  brand: string;
  model: string;
  cpu: string | null;
  gpu: string | null;
  ram_gb: number | null;
  ram_type: string | null;
  ram_speed_mhz: number | null;
  storage_gb: number | null;
  storage_type: string | null;
  storage_interface: string | null;
  screen_size: number | null;
  resolution: string | null;
  panel_type: string | null;
  refresh_rate_hz: number | null;
  os: string | null;
  offers: Offer[];
};

export async function getProducts(): Promise<Product[]> {
  const response = await fetch(`${API_BASE_URL}/products`, {
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error("Failed to fetch products");
  }

  return response.json();
}
