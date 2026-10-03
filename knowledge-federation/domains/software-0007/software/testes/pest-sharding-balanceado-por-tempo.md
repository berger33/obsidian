---
id: software.testes.tranche15.000883
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://pestphp.com/docs/optimizing-tests", "https://pestphp.com/docs/cli-api-reference"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pest 5: atualizar tempos para distribuir shards por duração

## Em uma frase
Sharding divide testes entre jobs de CI; Pest pode balancear os shards pelo tempo medido quando o arquivo de durações é gerado e versionado no projeto.

## Por que importa
Cortar apenas por número de arquivos pode deixar um job muito mais lento se alguns casos pesados se concentrarem numa partição.

## Como funciona
`--update-shards` escreve `tests/.pest/shards.json`, e `--shard=1/4` consulta esse artefato para distribuir arquivos conhecidos conforme o histórico.

## Exemplo
Rode `./vendor/bin/pest --update-shards`, revise e faça commit do JSON, depois execute cada job com `--shard=i/n`; no ciclo de manutenção, regenere os dados após mudanças relevantes.

## Limites e trade-offs
Arquivos novos ainda podem ser distribuídos de forma uniforme até que os tempos sejam atualizados, e um histórico antigo não prevê mudanças de custo em fixtures ou infraestrutura.

## Como verificar
Compare a duração dos quatro jobs ao atualizar o mapa, confirme a presença de todos os arquivos e investigue shards que ficaram muito diferentes em wall-clock.

## Conexões
- [[pest-ci-ignora-testes-focados-com-only]] — Veja também: Pest 5: fazer o job de CI ignorar focos locais marcados only.
- [[pest-parallel-nao-isola-recursos-externos]] — Veja também: Pest 5: desenhar testes independentes antes de habilitar parallel.

## Fontes
- [Pest 5 — Optimizing Tests](https://pestphp.com/docs/optimizing-tests) — parallel testing, profiling, sharding balanceado por tempo e saída; consultado em 2026-10-02.
- [Pest 5 — CLI API Reference](https://pestphp.com/docs/cli-api-reference) — opções de seleção, execução, paralelismo, shards e reporters; consultado em 2026-10-02.
