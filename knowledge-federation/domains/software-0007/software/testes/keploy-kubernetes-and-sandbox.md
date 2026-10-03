---
id: software.testes.tranche20.001395
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://keploy.io/docs/", "https://github.com/keploy/keploy"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Keploy: gravar em ambiente conteinerizado

## Em uma frase
A gravação pode ocorrer em ambiente conteinerizado, capturando tráfego de serviços em execução e reproduzindo-o depois em outro ambiente.

## Por que importa
Gravar em ambiente próximo do real e repetir localmente ou na esteira reduz a distância entre o comportamento observado e o verificado.

## Como funciona
Habilite a captura no ambiente de gravação, exercite os fluxos e transfira os artefatos para o ambiente de repetição.

## Exemplo
Um serviço em ambiente de homologação pode ter o tráfego coletado e o conjunto repetido no ambiente local do desenvolvedor.

## Limites e trade-offs
Permissões e recursos do ambiente de captura diferem entre máquinas, e dados sensíveis presentes no tráfego exigem tratamento antes do versionamento.

## Como verificar
Reproduza localmente os artefatos gravados em ambiente distinto e confirme que o resultado é equivalente.

## Conexões
- [[keploy-coverage-report]] — Veja também: Keploy: medir cobertura da repetição.
- [[keploy-multi-language]] — Veja também: Keploy: usar com diferentes linguagens.

## Fontes
- [Keploy — Documentação](https://keploy.io/docs/) — instalação, gravação de tráfego, repetição e integração; consultado em 2026-10-03.
- [Keploy — repositório oficial](https://github.com/keploy/keploy) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
