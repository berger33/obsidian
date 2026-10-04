---
id: software.testes.tranche19.001292
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
fontes: ["https://docs.localstack.cloud/getting-started/", "https://github.com/localstack/localstack"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# LocalStack: escolher entre estado limpo e persistente

## Em uma frase
A pasta montada preserva recursos entre reinícios quando a persistência está ativa, em oposição ao estado descartável.

## Por que importa
Testes de integração geralmente querem estado limpo, enquanto o desenvolvimento local se beneficia de recursos persistentes.

## Como funciona
Desative a persistência na esteira para começar do zero e ative-a no ambiente de desenvolvimento com limpeza periódica.

## Exemplo
O desenvolvedor pode manter um conjunto de dados de exemplo entre sessões, enquanto a esteira sempre parte de ambiente vazio.

## Limites e trade-offs
Persistência esquecida na esteira faz um teste passar por dado deixado por execução anterior, mascarando dependências.

## Como verificar
Execute a suíte duas vezes seguidas com persistência desligada e confirme que o resultado independe do estado anterior.

## Conexões
- [[localstack-docker-compose]] — Veja também: LocalStack: executar com composição de contêineres.
- [[localstack-testcontainers]] — Veja também: LocalStack: subir o ambiente dentro do teste.

## Fontes
- [LocalStack — Primeiros passos](https://docs.localstack.cloud/getting-started/) — instalação, execução local e visão geral dos serviços emulados; consultado em 2026-10-03.
- [LocalStack — repositório oficial](https://github.com/localstack/localstack) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
