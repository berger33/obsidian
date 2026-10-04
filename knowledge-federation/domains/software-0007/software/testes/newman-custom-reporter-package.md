---
id: software.testes.tranche12.000638
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
fontes: ["https://github.com/postmanlabs/newman/blob/develop/README.md#external-reporters", "https://github.com/postmanlabs/newman/blob/develop/README.md#reporters"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Newman: estender relatórios com reporter externo

## Em uma frase
Newman pode carregar reporters externos instalados como módulos Node compatíveis com a convenção de reporter.

## Por que importa
Uma extensão é útil quando o pipeline precisa de um formato corporativo ou anexos que os reporters incluídos não fornecem.

## Como funciona
Instale o pacote no ambiente do runner, use o nome de reporter conforme a documentação do módulo e mantenha a dependência fixada no lockfile.

## Exemplo
Um projeto pode instalar um reporter HTML externo localmente e solicitá-lo com os reporters CLI junto de JSON.

## Limites e trade-offs
Um pacote não instalado no mesmo contexto de resolução do Newman causa erro antes de executar a collection, e plugins podem precisar de atualização independente.

## Como verificar
Construa um job limpo a partir do lockfile e confirme que o reporter produz saída compatível com a versão do Newman fixada.

## Conexões
- [[newman-reporters-artifacts]] — Veja também: Newman: combinar reporters sem perder saída CLI.
- [[newman-programmatic-events-summary]] — Veja também: Newman: integrar collections pela API Node.

## Fontes
- [Newman — External Reporters](https://github.com/postmanlabs/newman/blob/develop/README.md#external-reporters) — instalação e carregamento de reporters externos; consultado em 2026-10-02.
- [Newman — Reporters](https://github.com/postmanlabs/newman/blob/develop/README.md#reporters) — reporters integrados, saídas CLI/JSON/JUnit e exportação de resultados; consultado em 2026-10-02.
