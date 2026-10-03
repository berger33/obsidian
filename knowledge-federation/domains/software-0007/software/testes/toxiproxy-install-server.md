---
id: software.testes.tranche21.001541
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/Shopify/toxiproxy", "https://github.com/Shopify/toxiproxy/blob/main/CHANGELOG.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Toxiproxy: obter e subir o servidor

## Em uma frase
O servidor é distribuído como binário e pacote (Linux via releases, macOS por Homebrew ou MacPorts, Windows via executável) e roda também como contêiner ghcr.io/shopify/toxiproxy; do fonte é make build.

## Por que importa
Decidir a instalação é só escolher o veículo: o serviço expõe a mesma API, e o Docker é o caminho natural em esteiras de contêiner.

## Como funciona
Suba o contêiner (com --net=host quando o host precisar alcançar o proxy) ou o binário, e valide com a chamada ao endpoint /version.

## Exemplo
docker run --rm ghcr.io/shopify/toxiproxy serve a API na porta padrão sem imagem própria de projeto.

## Limites e trade-offs
O build de fonte exige Go instalado; a página menciona ainda a interface CLI via --entrypoint="/toxiproxy-cli" no contêiner.

## Como verificar
Consulte /version no servidor recém-subido e confirme a compatibilidade com a biblioteca cliente escolhida.

## Conexões
- [[toxiproxy-purpose-positioning]] — Veja também: Toxiproxy: provar a resiliência em teste.
- [[toxiproxy-populate-proxies]] — Veja também: Toxiproxy: popular os proxies no boot.

## Fontes
- [Toxiproxy — README oficial](https://github.com/Shopify/toxiproxy) — proposta, instalação, populate, toxics e HTTP API; consultado em 2026-10-03.
- [Toxiproxy — CHANGELOG](https://github.com/Shopify/toxiproxy/blob/main/CHANGELOG.md) — histórico de releases e mudanças da API; consultado em 2026-10-03.
