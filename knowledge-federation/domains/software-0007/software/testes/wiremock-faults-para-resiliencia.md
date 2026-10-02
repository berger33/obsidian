---
id: software.testes.tranche11.000467
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://wiremock.org/docs/simulating-faults/", "https://wiremock.org/docs/verifying/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: usar faults controlados para testar tolerância a falha

## Em uma frase
WireMock pode simular falhas de transporte para observar como o cliente trata interrupções e respostas incompletas.

## Por que importa
WireMock devolve respostas configuradas para requests correspondentes e mantém evidência de tráfego recebido, permitindo isolar dependências sem substituir assertions do sistema testado. Testar somente 500 com corpo válido não cobre reset de conexão, atraso ou outras falhas na fronteira HTTP.

## Como funciona
Configure mappings próximos do caso, use matchers que expressem o contrato observado e isole servidor, request journal e cenários entre testes; verifique requests e respostas em vez de testar somente o stub. Escolha fault documentado e isolado, limite timeout do cliente e valide retry, fallback e registro de erro sem atingir sistemas externos.

## Exemplo
Um caso simula conexão interrompida e confirma que o client aplica retry limitado e encerra dentro do deadline.

## Limites e trade-offs
Um mock não prova a compatibilidade com serviço real. Journal e cenários possuem estado, matchers genéricos podem aceitar requests incorretos e extensões como templating exigem configuração explícita. Faults representam cenários artificiais e podem depender da versão de servidor e protocolo; não generalize para todos os erros de rede.

## Como verificar
Rode caso de sucesso e cada fault configurado e confirme número de tentativas, deadline e ausência de efeito duplicado.

## Conexões
- [[wiremock-unmatched-requests-near-miss]] — Veja também: WireMock: diagnosticar request não mapeada com near miss.
- [[wiremock-junit-extension-reset-por-teste]] — Veja também: WireMock: confirmar lifecycle e reset da extensão JUnit.

## Fontes
- [WireMock — Simulating Faults](https://wiremock.org/docs/simulating-faults/) — falhas de transporte e condições para testar resiliência; consultado em 2026-10-02.
- [WireMock — Verifying](https://wiremock.org/docs/verifying/) — request journal, verificações, requests não correspondidos e near misses; consultado em 2026-10-02.
