---
id: software.testes.tranche13.000708
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://onsi.github.io/gomega/#making-asynchronous-assertions", "https://pkg.go.dev/github.com/onsi/ginkgo/v2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gomega: usar Consistently para ausência durante janela

## Em uma frase
`Consistently` avalia matcher por uma janela temporal para verificar que condição permanece verdadeira ou comportamento indesejado não aparece.

## Por que importa
Uma única observação confirma somente um instante; janela repetida pode detectar evento atrasado ou vazamento que surge depois da ação.

## Como funciona
Escolha intervalo e duração proporcionais ao requisito e monitore função de leitura, não a ação que criaria o evento.

## Exemplo
Depois de revogar sessão, o teste verifica por um período curto que token antigo não volta a ser aceito pelo endpoint.

## Limites e trade-offs
Janela longa aumenta duração e não substitui prova de segurança ou teste de carga; comportamento pode surgir depois da janela escolhida.

## Como verificar
Faça callback mudar condição na metade da janela e confirme que assertion falha antes de completar o tempo configurado.

## Conexões
- [[ginkgo-eventually-context]] — Veja também: Gomega: limitar Eventually com contexto de spec.
- [[ginkgo-flake-attempts-evidence]] — Veja também: Ginkgo: deixar FlakeAttempts visível no relatório.

## Fontes
- [Gomega — Asynchronous Assertions](https://onsi.github.io/gomega/#making-asynchronous-assertions) — Eventually and Consistently polling assertions; consultado em 2026-10-02.
- [Ginkgo v2 — API Reference](https://pkg.go.dev/github.com/onsi/ginkgo/v2) — spec nodes, decorators and reports; consultado em 2026-10-02.
