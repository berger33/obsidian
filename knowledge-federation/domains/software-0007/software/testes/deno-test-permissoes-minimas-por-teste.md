---
id: software.testes.tranche15.000891
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
fontes: ["https://docs.deno.com/runtime/test/", "https://docs.deno.com/runtime/reference/cli/test/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Deno test: restringir permissões por teste sem ampliar a concessão da CLI

## Em uma frase
As opções de permissões de um Deno.test podem restringir o acesso daquele caso, mas não concedem capacidades que o comando deno test não autorizou.

## Por que importa
Uma permissão por teste não amplia a concessão global do runner; a CLI precisa autorizar primeiro a capacidade, e a configuração do caso pode então delimitar seu uso.

## Como funciona
Isso permite testar explicitamente caminhos autorizados e tentativas negadas.

## Exemplo
Execute `deno test --allow-read=./fixtures` e declare `permissions: { read: ["./fixtures"] }` apenas no caso que consome essas fixtures; mantenha outro caso sem leitura para validar a recusa.

## Limites e trade-offs
Sem a flag correspondente na CLI, a permissão solicitada pelo teste continua negada. Evite --allow-all no job, pois uma concessão ampla dificulta perceber dependências e reduz a utilidade da configuração por teste.

## Como verificar
Rode primeiro sem --allow-read e confirme a falha, depois com --allow-read=./fixtures; teste a leitura dentro e fora do diretório permitido e confirme que a opção do caso não concede além da CLI.

## Conexões
- [[deno-test-descoberta-de-arquivos-e-pastas]] — Veja também: Deno test: alinhar nome e localização às regras de descoberta.
- [[deno-test-steps-com-subcasos-hierarquicos]] — Veja também: Deno test: usar steps para estruturar uma operação com fases.

## Fontes
- [Deno Runtime — Testing](https://docs.deno.com/runtime/test/) — steps, timeouts, affected tests, permissões, snapshots, sanitizers e reporters; consultado em 2026-10-02.
- [Deno Runtime — deno test](https://docs.deno.com/runtime/reference/cli/test/) — flags de filtro, shard, cobertura, snapshots e execução do runner; consultado em 2026-10-02.
