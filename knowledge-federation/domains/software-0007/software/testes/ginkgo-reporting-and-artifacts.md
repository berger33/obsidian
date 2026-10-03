---
id: software.testes.tranche18.001214
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
fontes: ["https://onsi.github.io/ginkgo/", "https://github.com/onsi/ginkgo"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Ginkgo: gerar relatórios e evidências

## Em uma frase
A suíte produz relatórios com hierarquia de contêineres, permite saída consumível por máquina e grava arquivos de perfil para depuração.

## Por que importa
A hierarquia legível facilita entender qual cenário falhou e o perfil ajuda a investigar bloqueios e consumo excessivo.

## Como funciona
Gere o relatório detalhado como artefato, ative saída estruturada no pipeline e preserve perfis quando houver investigação de travamento.

## Exemplo
Um relatório em formato consumível faz a ferramenta de integração publicar cada especificação como caso próprio.

## Limites e trade-offs
Relatórios volumosos sem retenção definida ocupam espaço, e perfis gerados sem necessidade adicionam custo à execução.

## Como verificar
Compare o relatório de duas execuções e confirme que cada especificação aparece com resultado e duração próprios.

## Conexões
- [[ginkgo-suite-bootstrap]] — Veja também: Ginkgo: estruturar o ponto de entrada da suíte.
- [[ginkgo-focus-and-pending]] — Veja também: Ginkgo: focar, pendente e ignorar.

## Fontes
- [Ginkgo — Documentation](https://onsi.github.io/ginkgo/) — contêineres, nós de preparação, paralelismo, etiquetas e relatórios; consultado em 2026-10-03.
- [Ginkgo — repositório oficial](https://github.com/onsi/ginkgo) — código-fonte, exemplos e ferramenta de linha de comando; consultado em 2026-10-03.
