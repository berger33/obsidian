---
id: software.testes.tranche18.001215
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

# Ginkgo: focar, pendente e ignorar

## Em uma frase
É possível marcar especificações como focadas, pendentes de implementação ou ignoradas temporariamente, com aviso sobre o uso de foco.

## Por que importa
O foco acelera a investigação local, e a marcação de pendente evita esquecer cenários ainda não implementados.

## Como funciona
Use foco apenas durante a investigação, remova antes de integrar, e prefira a marcação de pendente com descrição do que falta.

## Exemplo
Uma especificação pode ficar pendente com texto explicando a dependência externa que impede sua implementação.

## Limites e trade-offs
Foco esquecido faz a suíte executar quase nada sem que ninguém perceba, e pendências antigas deixam cenários fora da verificação indefinidamente.

## Como verificar
Introduza foco em uma execução de teste e confirme que o relatório destaca o efeito sobre o conjunto executado.

## Conexões
- [[ginkgo-reporting-and-artifacts]] — Veja também: Ginkgo: gerar relatórios e evidências.
- [[ginkgo-cli-and-limits]] — Veja também: Ginkgo: operar a linha de comando e reconhecer limites.

## Fontes
- [Ginkgo — Documentation](https://onsi.github.io/ginkgo/) — contêineres, nós de preparação, paralelismo, etiquetas e relatórios; consultado em 2026-10-03.
- [Ginkgo — pacote publicado](https://pkg.go.dev/github.com/onsi/ginkgo/v2) — API pública, decoradores e funções de execução; consultado em 2026-10-03.
