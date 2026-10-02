---
id: software.testes.tranche12.000631
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

# Newman: fixar a origem da collection executada

## Em uma frase
`newman run` aceita uma collection exportada em arquivo JSON ou uma URL que forneça a definição da coleção.

## Por que importa
Fixar a origem torna a execução revisável e reduz a chance de um job depender de uma collection editada apenas na sessão local.

## Como funciona
Versione o arquivo exportado junto das mudanças relacionadas, ou documente a URL e autenticação necessárias quando a coleção vier de um serviço.

## Exemplo
Uma pipeline pode baixar a collection do repositório e passar seu caminho ao runner, usando o mesmo artefato em teste local e CI.

## Limites e trade-offs
Uma URL mutável pode apontar para conteúdo diferente em runs distintos; dados embutidos na exportação podem incluir exemplos sensíveis que precisam de revisão.

## Como verificar
Registre hash ou versão do JSON usado no job e compare com o artefato que o autor executou durante revisão.

## Conexões
- [[newman-maintenance-workflow-choice]] — Veja também: Newman: avaliar o modo de manutenção antes de expandir uso.
- [[newman-environment-global-precedence]] — Veja também: Newman: separar environment e globals.

## Fontes
- [Newman — README e opções](https://github.com/postmanlabs/newman/blob/develop/README.md) — estado de manutenção, CLI, opções, reporters e uso como biblioteca; consultado em 2026-10-02.
- [Newman — API Reference](https://github.com/postmanlabs/newman/blob/develop/README.md#api-reference) — newman.run, eventos e callback de conclusão; consultado em 2026-10-02.
