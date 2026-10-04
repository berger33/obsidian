---
id: software.testes.tranche18.001212
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://onsi.github.io/ginkgo/", "https://pkg.go.dev/github.com/onsi/ginkgo/v2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Ginkgo: selecionar especificações com etiquetas

## Em uma frase
Etiquetas aplicadas a especificações e contêineres podem ser combinadas em expressões para filtrar a execução por linha de comando.

## Por que importa
Recortes por tipo de teste ou área permitem rodar subconjuntos adequados ao momento sem duplicar arquivos.

## Como funciona
Aplique etiquetas com significado estável, combine-as em expressões explícitas e documente as usadas pelo pipeline.

## Exemplo
Uma execução de fumaça pode selecionar apenas as etiquetas de fluxo crítico e deixar a suíte completa para a etapa noturna.

## Limites e trade-offs
Expressões complexas dificultam prever o que será executado, e etiquetas duplicadas com grafias diferentes quebram o filtro silenciosamente.

## Como verificar
Liste as especificações selecionadas pela expressão e compare com a intenção antes de fixá-la.

## Conexões
- [[ginkgo-ordered-and-serial]] — Veja também: Ginkgo: declarar ordem e serialidade.
- [[ginkgo-suite-bootstrap]] — Veja também: Ginkgo: estruturar o ponto de entrada da suíte.

## Fontes
- [Ginkgo — Documentation](https://onsi.github.io/ginkgo/) — contêineres, nós de preparação, paralelismo, etiquetas e relatórios; consultado em 2026-10-03.
- [Ginkgo — pacote publicado](https://pkg.go.dev/github.com/onsi/ginkgo/v2) — API pública, decoradores e funções de execução; consultado em 2026-10-03.
