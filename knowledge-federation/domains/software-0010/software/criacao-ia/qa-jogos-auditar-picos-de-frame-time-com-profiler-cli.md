---
id: software.criacao_ia.tranche02.000190
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/", "https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/index.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Performance de Jogos: auditar picos de frame time com profiler em linha de comando

## Em uma frase
A captura automatizada de métricas de tempo de quadro (*frame time*) e alocação de memória (GC) evita o lançamento de versões com quedas de performance.

## Por que importa
Quedas bruscas de taxa de quadros (*spikes*) arruínam a fluidez de jogos de ação e podem causar enjoo visual em jogos de realidade virtual.

## Como funciona
Execute uma rota de teste padronizada gravando as durações individuais de cada quadro em milissegundos e reprove o build no CI se mais de 1% dos quadros excederem 16.6ms (para 60 FPS estáveis).

## Exemplo
```bash
# Executando benchmark de performance com relatorio em CSV
./MyGame.exe -benchmark -duration=120 -csvOutput=perf_results.csv
```

## Limites e trade-offs
Testes executados em máquinas virtuais de CI sem placas de vídeo dedicadas apresentam métricas de renderização incompatíveis com o hardware dos jogadores.

## Como verificar
Analise a planilha CSV gerada após a execução do benchmark e confirme a porcentagem de quadros que respeitaram o teto de 16.6ms.

## Conexões
- [[qa-jogos-isolar-cenarios-de-regressao-de-gameplay]] — Veja também: QA de Gameplay: criar microcenários isolados para regressão de mecânicas.
- [[assets-ia-otimizar-compressao-bc7-e-astc-em-vram]] — Conexão temática direta com assets-ia-otimizar-compressao-bc7-e-astc-em-vram.
- [[unreal-manter-renders-rastreaveis]] — Conexão temática direta com unreal-manter-renders-rastreaveis.
- [[qa-jogos-executar-playtests-headless-em-ci]] — Conexão temática direta com qa-jogos-executar-playtests-headless-em-ci.

## Fontes
- [Farama Gymnasium Documentation — Environment Creation](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/) — Guia padrão para criação de ambientes de reinforcement learning (step, reset, action/observation spaces). Consulta: 2026-10-04.
- [Unity Test Framework Manual](https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/index.html) — Documentação de testes de integração playmode, asserções de física e execução automatizada em ci. Consulta: 2026-10-04.
