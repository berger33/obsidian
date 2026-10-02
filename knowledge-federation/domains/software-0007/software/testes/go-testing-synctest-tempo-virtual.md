---
id: software.testes.tranche12.000586
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://pkg.go.dev/testing/synctest", "https://go.dev/doc/go1.25"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Go testing: coordenar concorrência com `testing/synctest`

## Em uma frase
`testing/synctest` executa código concorrente em uma bolha isolada com tempo virtual para testes que dependem de timers e goroutines.

## Por que importa
Substituir sleeps reais por avanço controlado do relógio reduz espera e flakiness em cenários cujo comportamento depende de tempo e bloqueio.

## Como funciona
Em Go 1.25, use `synctest.Test` para executar a função de teste na bolha e as operações documentadas para aguardar quiescência; mantenha I/O externo real fora das expectativas de tempo virtual.

## Exemplo
Um teste pode validar que um retry ocorre após um timer sem aguardar segundos de relógio real, deixando o scheduler avançar quando todas as goroutines da bolha estão bloqueadas.

## Limites e trade-offs
O mecanismo não transforma serviços remotos em dependências simuladas e código que sai da bolha continua exigindo sincronização apropriada.

## Como verificar
Rode um teste de timer com relógio virtual e confirme que o resultado independe de pausas arbitrárias da máquina de CI.

## Conexões
- [[go-race-dinamico-limites]] — Veja também: Go testing: alcance e limite do detector `-race`.
- [[go-testmain-recursos-pacote]] — Veja também: Go testing: centralizar preparação no `TestMain`.

## Fontes
- [Go — testing/synctest](https://pkg.go.dev/testing/synctest) — bolhas isoladas, tempo virtual e espera por goroutines bloqueadas; consultado em 2026-10-02.
- [Go 1.25 Release Notes — testing/synctest](https://go.dev/doc/go1.25) — estabilização de testing/synctest no Go 1.25 e mudança desde a fase experimental; consultado em 2026-10-02.
