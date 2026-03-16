import LaptopCard from "@/components/laptops/laptop-card";
import { getProducts } from "@/lib/api";

export default async function HomePage() {
  const products = await getProducts();

  return (
    <main className="min-h-screen bg-gray-50 px-6 py-10">
      <div className="mx-auto max-w-6xl">
        <h1 className="text-4xl font-bold tracking-tight text-gray-900">
          Laptop Price Tracker
        </h1>
        <p className="mt-2 text-gray-600">
          Track gaming laptops by specs, prices, and retailers.
        </p>

        <div className="mt-8 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
          {products.length > 0 ? (
            products.map((product) => (
              <LaptopCard key={product.id} product={product} />
            ))
          ) : (
            <p className="text-gray-600">No products found.</p>
          )}
        </div>
      </div>
    </main>
  );
}
