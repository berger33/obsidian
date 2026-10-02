---
id: software.testes.tranche12.000635
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
fontes: ["https://github.com/postmanlabs/newman/blob/develop/README.md", "https://github.com/postmanlabs/newman/blob/develop/README.md#api-reference"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Newman: decidir entre interromper cedo e preservar diagnóstico

## Em uma frase
`--bail` pode interromper a execução ao encontrar erro em script de teste, e `--suppress-exit-code` substitui o código padrão do runner.

## Por que importa
Interromper cedo reduz custo após uma falha decisiva, enquanto uma execução completa pode revelar outros defeitos no mesmo build.

## Como funciona
Use `--bail failure` para encerrar após concluir o script de teste que falhou; configure `--suppress-exit-code` somente fora de gates que dependem do status de saída.

## Exemplo
Um smoke check pode parar no primeiro erro de autenticação; um job noturno pode continuar a collection para reunir relatório de todas as rotas.

## Limites e trade-offs
`--bail failure` interrompe depois do script de teste atual, não necessariamente na primeira assertion; suprimir o exit code pode mascarar o resultado vermelho em CI.

## Como verificar
Force uma assertion a falhar e confira tanto os requests executados quanto o status final observado pelo shell ou pelo orquestrador.

## Conexões
- [[newman-folder-selection]] — Veja também: Newman: restringir execução a pastas da collection.
- [[newman-timeout-scopes]] — Veja também: Newman: distinguir timeout total, de request e de script.

## Fontes
- [Newman — README e opções](https://github.com/postmanlabs/newman/blob/develop/README.md) — estado de manutenção, CLI, opções, reporters e uso como biblioteca; consultado em 2026-10-02.
- [Newman — API Reference](https://github.com/postmanlabs/newman/blob/develop/README.md#api-reference) — newman.run, eventos e callback de conclusão; consultado em 2026-10-02.
