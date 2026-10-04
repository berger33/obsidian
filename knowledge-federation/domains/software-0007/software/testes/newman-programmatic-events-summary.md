---
id: software.testes.tranche12.000639
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
fontes: ["https://github.com/postmanlabs/newman/blob/develop/README.md#api-reference", "https://github.com/postmanlabs/newman/blob/develop/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Newman: integrar collections pela API Node

## Em uma frase
A API programática expõe `newman.run`, callback e eventos para iniciar collections de dentro de uma aplicação Node.

## Por que importa
Integração como biblioteca permite que um sistema de build controle configuração e consuma resumo sem invocar um subprocesso de CLI.

## Como funciona
Passe a collection e as opções à função `run`, trate erros do callback e use os eventos documentados para coletar progresso sem interpretar texto do terminal.

## Exemplo
Um serviço de QA pode executar a mesma collection após provisionar ambiente e gravar o resumo estruturado na plataforma interna.

## Limites e trade-offs
A aplicação hospedeira passa a ser responsável por propagar falhas e encerrar o processo no status correto; ignorar o callback pode criar falso sucesso.

## Como verificar
Simule erro de execução e sucesso numa aplicação mínima e confirme que o chamador recebe ambos os estados e aguarda o evento de conclusão.

## Conexões
- [[newman-custom-reporter-package]] — Veja também: Newman: estender relatórios com reporter externo.

## Fontes
- [Newman — API Reference](https://github.com/postmanlabs/newman/blob/develop/README.md#api-reference) — newman.run, eventos e callback de conclusão; consultado em 2026-10-02.
- [Newman — README e opções](https://github.com/postmanlabs/newman/blob/develop/README.md) — estado de manutenção, CLI, opções, reporters e uso como biblioteca; consultado em 2026-10-02.
