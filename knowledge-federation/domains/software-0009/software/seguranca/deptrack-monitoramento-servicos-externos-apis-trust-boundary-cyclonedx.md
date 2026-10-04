---
id: software.seguranca.tranche01.000037
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/DependencyTrack/dependency-track/master/README.md", "https://docs.dependencytrack.org/getting-started/initial-startup/", "https://github.com/DependencyTrack/dependency-track"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP Dependency-Track Inventário de Serviços e APIs: rastreamento de provedores externos, classificação de dados e *Trust Boundaries*

## Em uma frase
Além de bibliotecas de software, o Dependency-Track suporta a seção `services` da especificação **CycloneDX**, permitindo inventariar e auditar **APIs e serviços externos** consumidos pela aplicação — registrando o provedor, URIs de endpoint, classificação de dados (*Data Classification*), direção do fluxo de dados (*inbound*/*outbound*/*bi-directional*), travessia de fronteira de confiança (*Trust Boundary traversal*) e requisitos de autenticação.

## Por que importa
Uma aplicação moderna não depende apenas de pacotes npm/Maven: ela envia dados sensíveis de clientes para APIs externas de pagamento, LLMs e analytics; um SBOM completo (*SaaSBOM* / *Service Inventory*) documenta essas dependências de serviço.

## Como funciona
Quando o SBOM CycloneDX declara entradas em `services[]`, o Dependency-Track popula a aba **Services** do projeto, permitindo à equipe de segurança e privacidade (LGPD/GDPR) auditar quais serviços externos recebem dados PII e se exigem autenticação.

## Exemplo
```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.5",
  "services": [
    {
      "name": "payment-gateway-api",
      "provider": { "name": "ExamplePay Inc." },
      "endpoints": [ "https://api.examplepay.com/v2/charges" ],
      "authenticated": true,
      "x-trust-boundary": true
    }
  ]
}
```

## Limites e trade-offs
Incluir os serviços externos consumidos no manifesto CycloneDX transforma o Dependency-Track em uma fonte única de verdade tanto para dependências de código quanto para integrações de APIs de terceiros.

## Como verificar
Inspecione os serviços registrados em um projeto via `GET /api/v1/service/project/{uuid}`.

## Conexões
- [[deptrack-impact-analysis-portfolio-busca-componentes-afetados-log4shell]] — Veja também: OWASP Dependency-Track Portfolio Impact Analysis: resposta imediata a incidentes (*"O que está afetado, e onde?"*) via PURL e CPE.
- [[deptrack-notificacoes-webhooks-slack-jira-defectdojo-integracoes]] — Veja também: OWASP Dependency-Track Notificações e Integrações: alertas em tempo real (`Slack`, `Teams`, `Jira`, `Webhooks`) e sincronização com `DefectDojo`.

## Fontes
- [OWASP Dependency-Track GitHub — README.md (Continuous SBOM Analysis Platform, CycloneDX, VEX, EPSS, Policy Engine & Ecosystem Integrations)](https://raw.githubusercontent.com/DependencyTrack/dependency-track/master/README.md) — README oficial do DependencyTrack/dependency-track documentando arquitetura API-first, consumo de SBOM CycloneDX, fontes de inteligência, EPSS e VEX; consultado em 2026-10-03.
- [OWASP Dependency-Track Official Documentation — Initial Startup & Operational Configuration (Admin Setup, Feeds, Mirroring & Portfolio Management)](https://docs.dependencytrack.org/getting-started/initial-startup/) — Documentação oficial de inicialização e operação do Dependency-Track cobrindo provisionamento, sincronização de bases NVD/OSV/EPSS e controle de acesso; consultado em 2026-10-03.
- [OWASP Dependency-Track — Official GitHub Repository](https://github.com/DependencyTrack/dependency-track) — Repositório oficial Apache-2.0 do OWASP Dependency-Track; consultado em 2026-10-03.
