---
id: software.testes.tranche19.001286
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/bbyars/mountebank", "https://www.mbtest.org/docs/api/overview"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mountebank: integrar ao pipeline

## Em uma frase
O serviço pode subir como processo ou contêiner na esteira, e os impostores são criados por configuração antes dos testes.

## Por que importa
Executar o serviço virtual na esteira elimina dependências externas instáveis e torna o resultado do build reproduzível.

## Como funciona
Suba o serviço antes da suíte, aguarde a disponibilidade da porta, carregue a configuração e derrube tudo ao final.

## Exemplo
A esteira pode iniciar o contêiner, executar os testes de integração e publicar o resumo das requisições registradas como evidência.

## Limites e trade-offs
Sem espera pela porta, os primeiros testes falham por indisponibilidade, e contêineres órfãos consomem recursos entre execuções.

## Como verificar
Execute o fluxo do zero duas vezes e confirme que o resultado é idêntico e que nenhum processo permanece ativo.

## Conexões
- [[mountebank-file-based-setup]] — Veja também: Mountebank: manter impostores em arquivo.
- [[mountebank-limits-and-practices]] — Veja também: Mountebank: reconhecer limites.

## Fontes
- [Mountebank — repositório oficial](https://github.com/bbyars/mountebank) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
- [Mountebank — API overview](https://www.mbtest.org/docs/api/overview) — interface administrativa, criação de impostores e remoção; consultado em 2026-10-03.
