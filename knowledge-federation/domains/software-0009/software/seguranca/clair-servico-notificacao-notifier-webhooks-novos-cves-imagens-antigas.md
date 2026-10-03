---
id: software.seguranca.tranche07.000695
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://quay.github.io/clair/whatis.html", "https://raw.githubusercontent.com/quay/clair/main/README.md", "https://quay.github.io/claircore/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Clair v4 (`Notifier`): Detecção Proativa de **Novos CVEs** em Imagens Já Implantadas e Entrega Confiável via **Webhooks / AMQP / STOMP**

## Em uma frase
O grande diferencial operacional de um scanner baseado em serviço contínuo como o Clair v4 frente a um scanner executado apenas no momento do build de CI é o serviço **`Notifier`**: o que acontece quando uma imagem foi construída limpa há 20 dias, está rodando em produção hoje, e um novo CVE crítico é publicado hoje à tarde?

## Por que importa
O **`Notifier`** monitora continuamente a tabela de `update_operations` do `Matcher`: sempre que qualquer Updater ingere novas vulnerabilidades ou atualiza um boletim, o `Notifier` calcula o *diff* entre a operação anterior e a nova, identifica imediatamente **todos os manifestos de imagens já indexados no passado que passaram a ser afetados pelo novo CVE** e cria uma **Notification** paginada!

## Como funciona
O `Notifier` entrega essas notificações de forma confiável para o Registry (**Project Quay**), SOAR ou SIEM através de **Webhooks HTTP assinados**, filas **AMQP (RabbitMQ)** ou **STOMP**, permitindo abrir tickets automáticos no DefectDojo/TheHive sem precisar re-escanear as imagens manualmente.

## Exemplo
```yaml
# Trecho do config.yaml do Clair v4 configurando o servico Notifier para enviar Webhooks assinados ao SOC
notifier:
  indexer_addr: "http://clair-indexer:6060"
  matcher_addr: "http://clair-matcher:6060"
  connstring: "host=clair-db port=5432 user=clair dbname=clair sslmode=verify-full"
  poll_interval: 5m
  delivery_interval: 1m
  webhook:
    target: "https://soar.soc.internal.corp/webhooks/clair-notifications"
    callback: "http://clair-notifier:6060/notifier/api/v1/notification/"
```

## Limites e trade-offs
Assim que o consumidor do webhook terminar de processar todas as páginas da notificação (`GET /notifier/api/v1/notification/{notification_id}`), ele deve enviar **`DELETE /notifier/api/v1/notification/{notification_id}`** para marcar a notificação como entregue e liberar os registros na fila do `Notifier`.

## Como verificar
Verifique nos logs do `Notifier` a execução do ciclo `poll_interval` após uma atualização de feed do `Matcher`.

## Conexões
- [[clair-motor-matching-updaters-fontes-ovals-osv-cvss-enrichment]] — Veja também: Clair v4 (`Matcher`): Atualizadores Contínuos de Feeds de Segurança (OVAL, **OSV**, Red Hat VEX/CSAF, Debian/Ubuntu/Alpine SecDB e NVD CVSS Enrichment).
- [[clair-cli-clairctl-client-submissao-manifestos-exportacao-offline]] — Veja também: Clair v4 (`clairctl`): Operação via Linha de Comando (`clairctl report`, `export-updaters` / `import-updaters`) para CI/CD e Ambientes *Air-Gapped*.
- [[clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier]] — Referência cruzada direta com clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier.

## Fontes
- [Project Quay Clair v4 Official Documentation — What is ClairV4 & Architecture](https://quay.github.io/clair/whatis.html) — documentação oficial do Clair v4 cobrindo a separação ClairCore, Indexer (IndexReport), Matcher (VulnerabilityReport) e Notifier; consultado em 2026-10-03.
- [Project Quay Clair Official GitHub — Container Vulnerability Static Analysis](https://raw.githubusercontent.com/quay/clair/main/README.md) — repositório oficial do projeto Clair v4 e utilitário de linha de comando clairctl; consultado em 2026-10-03.
- [ClairCore Official Documentation — Layer Indexing & Vulnerability Matching Engine](https://quay.github.io/claircore/) — documentação oficial da biblioteca ClairCore para extração de pacotes de SO/linguagens e updaters de vulnerabilidades; consultado em 2026-10-03.
