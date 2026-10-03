---
id: software.testes.tranche19.001289
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
fontes: ["https://docs.localstack.cloud/aws/capabilities/config/initialization-hooks/", "https://docs.localstack.cloud/getting-started/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# LocalStack: preparar recursos com ganchos de inicialização

## Em uma frase
Scripts em diretórios de fases distintas são executados na subida, quando o serviço fica pronto e no encerramento do contêiner.

## Por que importa
Provisionar recursos na fase correta garante que eles existam antes do primeiro teste, sem passos manuais.

## Como funciona
Monte os scripts no diretório da fase adequada, torne-os executáveis e use a ferramenta de linha de comando apontada para o ambiente emulado.

## Exemplo
Um script pode criar a fila e o tópico usados pelos testes assim que o serviço fica pronto.

## Limites e trade-offs
Scripts na fase errada executam antes de o serviço aceitar chamadas, e arquivos sem permissão de execução são ignorados.

## Como verificar
Consulte o ponto de estado da inicialização e confirme que a fase desejada aparece concluída antes dos testes.

## Conexões
- [[localstack-service-emulation]] — Veja também: LocalStack: emular serviços de nuvem localmente.
- [[localstack-init-troubleshooting]] — Veja também: LocalStack: diagnosticar ganchos que não executam.

## Fontes
- [LocalStack — Initialization hooks](https://docs.localstack.cloud/aws/capabilities/config/initialization-hooks/) — fases de inicialização, diretórios e ponto de estado; consultado em 2026-10-03.
- [LocalStack — Primeiros passos](https://docs.localstack.cloud/getting-started/) — instalação, execução local e visão geral dos serviços emulados; consultado em 2026-10-03.
