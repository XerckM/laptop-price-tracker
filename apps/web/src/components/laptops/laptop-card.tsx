type LaptopCardProps = {
  product: {
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
  };
};

export default function LaptopCard({ product }: LaptopCardProps) {
  return (
    <div className="rounded-2xl border border-gray-200 p-5 shadow-sm bg-white">
      <h2 className="text-xl font-semibold">
        {product.brand} {product.model}
      </h2>

      <div className="mt-3 space-y-1 text-sm text-gray-700">
        <p><span className="font-medium">CPU:</span> {product.cpu ?? "N/A"}</p>
        <p><span className="font-medium">GPU:</span> {product.gpu ?? "N/A"}</p>
        <p>
          <span className="font-medium">RAM:</span>{" "}
          {product.ram_gb ?? "N/A"} GB
          {product.ram_type ? ` ${product.ram_type}` : ""}
          {product.ram_speed_mhz ? ` @ ${product.ram_speed_mhz} MHz` : ""}
        </p>
        <p>
          <span className="font-medium">Storage:</span>{" "}
          {product.storage_gb ?? "N/A"} GB
          {product.storage_type ? ` ${product.storage_type}` : ""}
          {product.storage_interface ? ` (${product.storage_interface})` : ""}
        </p>
        <p>
          <span className="font-medium">Display:</span>{" "}
          {product.screen_size ?? "N/A"}″
          {product.resolution ? ` ${product.resolution}` : ""}
          {product.panel_type ? ` ${product.panel_type}` : ""}
          {product.refresh_rate_hz ? ` ${product.refresh_rate_hz}Hz` : ""}
        </p>
        <p><span className="font-medium">OS:</span> {product.os ?? "N/A"}</p>
      </div>
    </div>
  );
}
