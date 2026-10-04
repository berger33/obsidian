---
id: software.seguranca.tranche01.000041
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
fontes: ["https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md", "https://www.zaproxy.org/docs/automate/automation-framework/", "https://github.com/zaproxy/zaproxy"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP ZAP (Zed Attack Proxy): arquitetura de proxy interceptador, `Passive Scanner` e `Active Scanner` para DAST

## Em uma frase
O **Zed Attack Proxy (ZAP)** (licenciado sob Apache 2.0) é o scanner open-source de segurança de aplicações web e APIs (**DAST — *Dynamic Application Security Testing***) mais utilizado do mundo, combinando um proxy de interceptação HTTP/HTTPS/WebSockets, crawlers automatizados (`Spider` / `Ajax Spider`), um **Passive Scanner** não-intrusivo e um **Active Scanner** de ataques simulados.

## Por que importa
Testes estáticos de código (SAST) não enxergam cabeçalhos HTTP ausentes configurados no proxy reverso (`Content-Security-Policy`, `Strict-Transport-Security`), cookies sem `HttpOnly`/`Secure`, falhas de CORS ou vulnerabilidades de roteamento em tempo de execução.

## Como funciona
No ZAP: 1) todo tráfego que passa pelo proxy ou que é descoberto pelos spiders é inspecionado automaticamente em background pelo **Passive Scanner** (que analisa apenas as requisições e respostas existentes, sem enviar nenhum pacote extra nem alterar dados); e 2) o **Active Scanner** envia requisições maliciosas controladas (SQLi, XSS, Path Traversal, Command Injection) contra os alvos autorizados no **Context**.

## Exemplo
```bash
# Executando o ZAP em modo headless com o Automation Framework via container oficial:
docker run --rm -v "$(pwd):/zap/wrk/:rw" \
  ghcr.io/zaproxy/zaproxy:stable \
  zap.sh -cmd -autorun /zap/wrk/zap-plan.yaml
```

## Limites e trade-offs
Execute o **Active Scanner** apenas contra ambientes de homologação/staging ou alvos onde você possui permissão explícita para testes intrusivos, pois ele submete formulários e injeta payloads reais.

## Como verificar
Execute `zap.sh -version` ou suba o container `ghcr.io/zaproxy/zaproxy:stable` para validar o ambiente de execução.

## Conexões
- [[zaproxy-automation-framework-yaml-env-jobs-substituicao-packaged-scans]] — Veja também: ZAP Automation Framework (`zap.sh -cmd -autorun`): controle declarativo em arquivo YAML único para CI/CD.

## Fontes
- [OWASP ZAP Official Documentation — Automation Framework (Declarative YAML Plan, env Contexts, Discovery/Scan/Report Jobs & Job Tests)](https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md) — Documentação oficial do Automation Framework do OWASP ZAP detalhando a estrutura YAML env/jobs, substituição dos Packaged Scans e lista completa de jobs suportados; consultado em 2026-10-03.
- [OWASP ZAP GitHub — README.md (Zed Attack Proxy Architecture, Passive & Active Scanners, Container Images & Add-ons)](https://www.zaproxy.org/docs/automate/automation-framework/) — README oficial do zaproxy/zaproxy apresentando o projeto DAST open-source, modos de execução headless e ecossistema de extensões; consultado em 2026-10-03.
- [OWASP ZAP — Official GitHub Repository](https://github.com/zaproxy/zaproxy) — Repositório oficial Apache-2.0 do OWASP Zed Attack Proxy; consultado em 2026-10-03.
