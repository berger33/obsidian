---
id: software.testes.tranche19.001287
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
fontes: ["https://www.mbtest.org/docs/api/proxies", "https://github.com/bbyars/mountebank"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mountebank: reconhecer limites

## Em uma frase
Simular serviços permite verificar o cliente contra respostas controladas, mas não valida o contrato real nem o comportamento do provedor.

## Por que importa
Confundir simulação com verificação de contrato deixa a integração real sem cobertura até a primeira execução conjunta.

## Como funciona
Complemente a simulação com testes de contrato ou execuções periódicas contra o serviço real e mantenha os exemplos gravados atualizados.

## Exemplo
Um cliente pode passar em todos os testes simulados e falhar na integração por divergência de formato que a simulação não captura.

## Limites e trade-offs
Simulações desatualizadas dão falsa segurança, e o excesso de lógica no serviço virtual cria um segundo sistema a manter.

## Como verificar
Compare a simulação com uma chamada real do mesmo endpoint e registre as divergências encontradas.

## Conexões
- [[mountebank-ci-integration]] — Veja também: Mountebank: integrar ao pipeline.

## Fontes
- [Mountebank — Proxies](https://www.mbtest.org/docs/api/proxies) — encaminhamento ao serviço real, gravação e reprodução; consultado em 2026-10-03.
- [Mountebank — repositório oficial](https://github.com/bbyars/mountebank) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
