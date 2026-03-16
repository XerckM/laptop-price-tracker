import { Product } from "@/lib/api";

type LaptopCardProps = {
  product: Product;
};

export default function LaptopCard({ product }: LaptopCardProps) {
  const lowestOffer =
    product.offers.length > 0
      ? [...product.offers].sort(
          (a, b) => Number(a.price) - Number(b.price)
        )[0]
      : null;

  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
      <h2 className="text-xl font-semibold text-gray-900">
        {product.brand} {product.model}
      </h2>

      {lowestOffer ? (
        <div className="mt-3 rounded-xl bg-green-50 p-3">
          <p className="text-lg font-bold text-green-700">
            ${Number(lowestOffer.price).toFixed(2)}
          </p>
          <p className="text-sm text-gray-700">
            {lowestOffer.retailer_name} ·{" "}
            {lowestOffer.in_stock ? "In Stock" : "Out of Stock"}
          </p>
          <a
            href={lowestOffer.url}
            target="_blank"
            rel="noreferrer"
            className="mt-1 inline-block text-sm font-medium text-blue-600 hover:underline"
          >
            View Offer
          </a>
        </div>
      ) : (
        <p className="mt-3 text-sm text-gray-500">No offers available.</p>
      )}

      <div className="mt-4 space-y-1 text-sm text-gray-700">
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
