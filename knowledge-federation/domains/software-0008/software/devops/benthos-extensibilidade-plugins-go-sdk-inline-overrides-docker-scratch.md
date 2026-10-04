---
id: software.devops.tranche20.002000
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/redpanda-data/connect/main/README.md", "https://docs.redpanda.com/redpanda-connect/about", "https://github.com/redpanda-data/connect"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Redpanda Connect Extensibilidade e Deploy: plugins customizados em Go (`public/service`), overrides `-s` e imagem OCI `scratch`

## Em uma frase
Fechando o lote de 2.000 notas de DevOps, o Redpanda Connect / Benthos oferece um **SDK público em Go (`github.com/redpanda-data/benthos/v4/public/service`)** para registrar inputs, processors e outputs customizados em poucas linhas de código, suporte à tag de compilação `x_benthos_extra` (para conectores CGo como `zmq4`), **inline overrides (`-s`)** na CLI e distribuição em imagem OCI mínima baseada em **`scratch`**.

## Por que importa
Em ambientes corporativos com protocolos legados internos ou bibliotecas de criptografia próprias em Go, poder compilar um binário único do Redpanda Connect contendo seu próprio plugin customizado (junto com todos os conectores oficiais) elimina gambiarras de sidecars.

## Como funciona
Na implantação via Docker ou Kubernetes, a flag **`-s` (`--set`)** permite sobrescrever ou injetar qualquer caminho do YAML via linha de comando (ex.: `-s "input.type=http_server" -s "output.kafka.addresses=kafka:9092"`), combinada com interpolação de variáveis de ambiente `${VAR:default}` dentro do arquivo de configuração.

## Exemplo
```bash
# Executando a imagem oficial scratch do Redpanda Connect com overrides inline via flag -s:
docker run --rm -p 4195:4195 docker.redpanda.com/redpandadata/connect run \
  -s "input.type=http_server" \
  -s "output.type=stdout"
```

## Limites e trade-offs
Conforme documentado no README oficial, componentes que dependem de bibliotecas C externas (como `zmq4`) exigem compilar o binário com `-tags "x_benthos_extra"` e ter as bibliotecas do sistema instaladas.

## Como verificar
Execute `docker run --rm docker.redpanda.com/redpandadata/connect list inputs` para listar todos os conectores disponíveis no binário.

## Conexões
- [[benthos-streams-mode-multiplexacao-pipelines-rest-api-resources]] — Veja também: Redpanda Connect `Streams Mode` e `Resources`: execução de múltiplos pipelines independentes em um único processo e API HTTP.

## Fontes
- [Redpanda Connect GitHub — README.md (Declarative Stream Processor, At-Least-Once Transaction Model, CDC to Iceberg, /ping & /ready Probes)](https://raw.githubusercontent.com/redpanda-data/connect/main/README.md) — README oficial do redpanda-data/connect detalhando instalação, execução via Docker/CLI, exemplo de Postgres CDC para Iceberg, probes HTTP e SDK de extensibilidade em Go; consultado em 2026-10-03.
- [Redpanda Connect Official Documentation — About Redpanda Connect (Bloblang Mapping, Stateless In-Process Transactions, Batching, Branching & Observability)](https://docs.redpanda.com/redpanda-connect/about) — Documentação oficial de arquitetura do Redpanda Connect / Benthos cobrindo garantias de entrega, Bloblang, conectores e operação cloud-native; consultado em 2026-10-03.
- [Redpanda Connect (Benthos) — Official GitHub Repository](https://github.com/redpanda-data/connect) — Repositório oficial do Redpanda Connect / Benthos; consultado em 2026-10-03.
