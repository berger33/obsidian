---
id: software.seguranca.tranche11.001040
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/README.md", "https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/pyproject.toml", "https://raw.githubusercontent.com/MobSF/mobsfscan/main/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Implantação Corporativa Segura do MobSF: Autenticação **SAML 2.0 SSO (`python3-saml`)**, Banco **PostgreSQL**, Filas Assíncronas (`django-q2`) e Hardening

## Em uma frase
Quando o MobSF deixa de rodar apenas no laptop individual de um pentester e passa a ser implantado como a **Plataforma Central de Segurança Mobile da Empresa** (recebendo binários confidenciais de pré-lançamento de todas as tribos de engenharia e pipelines de CI/CD), rodá-lo com SQLite e conta compartilhada `mobsf/mobsf` não é adequado.

## Por que importa
Conforme mostram as dependências oficiais no `pyproject.toml` (`python3-saml`, `psycopg2-binary`, `django-q2`, `django-ratelimit`, `gunicorn`), o MobSF possui suporte empresarial completo para: **(1) Autenticação e Controle de Acesso Baseado em Papéis (RBAC) com SAML 2.0 Single Sign-On (SSO)** integrado ao **Okta, Microsoft Entra ID, Keycloak ou CNCF Dex**; **(2) Banco de Dados PostgreSQL externo** (`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, `POSTGRES_HOST`); e **(3) Filas de Tarefas Assíncronas (`django-q2`)** para processar múltiplos uploads pesados em paralelo!

## Como funciona
Além disso, como o MobSF processa arquivos enviados por usuários, ele utiliza `defusedxml` (contra ataques XXE em manifestos XML) e `django-ratelimit`!

## Exemplo
```bash
# Implantar o MobSF em producao conectado a um banco PostgreSQL dedicado e desativando autenticacao padrao em favor de SSO/API Key
docker run -d --name mobsf-enterprise \
  -p 127.0.0.1:8000:8000 \
  -e MOBSF_DISABLE_AUTHENTICATION="0" \
  -e POSTGRES_USER="mobsf_prod" \
  -e POSTGRES_PASSWORD="${MOBSF_DB_PASSWORD}" \
  -e POSTGRES_DB="mobsf" \
  -e POSTGRES_HOST="postgres.secops.internal" \
  -v /srv/mobsf_data:/home/mobsf/.MobSF \
  opensecurity/mobile-security-framework-mobsf:latest
```

## Limites e trade-offs
Ao expor o MobSF corporativo na intranet, coloque-o atrás de um proxy reverso **Pomerium** ou **Authelia / NGINX** com TLS 1.3 (`-p 127.0.0.1:8000:8000`), restrinja o tamanho máximo de upload e isole o container do MobSF em uma rede sem acesso aos sistemas internos de produção (exceto o banco PostgreSQL do próprio MobSF e os emuladores de laboratório).

## Como verificar
Faça backup regular do volume `/home/mobsf/.MobSF` e do banco PostgreSQL para preservar o histórico de Scorecards e comparações entre versões.

## Conexões
- [[mobsf-auditoria-segredos-entropia-firebase-aws-google-services-json]] — Veja também: Caça a Credenciais Cloud e **Bancos Firebase Abertos (`google-services.json` / `GoogleService-Info.plist`)** em Aplicativos Mobile com MobSF.
- [[mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx]] — Referência cruzada direta com mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx.
- [[mobsf-automacao-api-rest-cicd-pdf-json-scorecard-diff]] — Referência cruzada direta com mobsf-automacao-api-rest-cicd-pdf-json-scorecard-diff.

## Fontes
- [Mobile Security Framework (MobSF) Official GitHub — All-in-One Mobile SAST, DAST & Malware Analysis](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/README.md) — repositório oficial do MobSF cobrindo análise estática e dinâmica de pacotes Android (APK/AAB), iOS (IPA) e Windows (APPX); consultado em 2026-10-03.
- [MobSF Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/pyproject.toml) — especificação oficial dos motores integrados no MobSF 4.5+ (`libsast`, `apkid`, `apksigtool`, `lief`, `macholib`, `frida`, `http-tools`, `python3-saml`); consultado em 2026-10-03.
- [MobSF `mobsfscan` Official GitHub — Shift-Left Static Analysis CLI for Android & iOS Source Code](https://raw.githubusercontent.com/MobSF/mobsfscan/main/README.md) — documentação oficial do `mobsfscan` cobrindo análise SAST de código Java/Kotlin/Swift/ObjC e exportação SARIF/SonarQube; consultado em 2026-10-03.
