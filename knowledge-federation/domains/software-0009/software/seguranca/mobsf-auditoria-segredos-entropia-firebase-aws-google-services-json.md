---
id: software.seguranca.tranche11.001039
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

# Caça a Credenciais Cloud e **Bancos Firebase Abertos (`google-services.json` / `GoogleService-Info.plist`)** em Aplicativos Mobile com MobSF

## Em uma frase
Um dos vetores mais críticos e recorrentes em aplicativos Android e iOS é a inclusão de configurações inseguras nos arquivos **`res/values/strings.xml`** (gerados a partir do **`google-services.json`** no Android) e **`GoogleService-Info.plist`** (no iOS).

## Por que importa
Quando o desenvolvedor inclui o SDK do **Google Firebase** ou **AWS Amplify** no app, o compilador empacota dentro do binário a URL do **Firebase Realtime Database (`https://<projeto>.firebaseio.com`)**, o bucket do **Google Cloud Storage / Firebase Storage (`<projeto>.appspot.com`)**, a **`google_api_key` (`AIzaSy...`)** e IDs de **Amazon Cognito Identity Pools**!

## Como funciona
O MobSF extrai automaticamente esses identificadores na seção **`Firebase DB / Hardcoded Secrets`** e testa se o endpoint **`https://<projeto>.firebaseio.com/.json`** está publicamente aberto para leitura sem autenticação (`200 OK`) — uma falha que já expôs dados pessoais de milhões de usuários em aplicativos móveis!

## Exemplo
```bash
# Extrair do relatorio JSON do MobSF todas as URLs de Firebase detectadas e os segredos de alta entropia encontrados no binario
MOBSF_API_KEY="sua_chave_api_mobsf_aqui"
FILE_HASH="4a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d"

curl -sS --request POST "http://127.0.0.1:8000/api/v1/report_json" \
  -H "X-Mobsf-Api-Key: ${MOBSF_API_KEY}" \
  -d "hash=${FILE_HASH}" | jq '{firebase_urls: .firebase_urls, secrets: .secrets}'
```

## Limites e trade-offs
Como corrigir definitivamente alertas de Firebase e chaves `AIzaSy...` no MobSF? **(1)** Nas regras de segurança do **Firebase Realtime Database / Cloud Firestore / Storage**, nunca use `.read: true` ou `allow read, write: if true` (exija sempre `request.auth != null` com validação de `request.auth.uid`); e **(2)** No Google Cloud Console, restrinja toda chave de API **`AIzaSy...`** tanto por **APIs permitidas** quanto por **Identificador do App (`Package Name` + `SHA-1 certificate fingerprint` no Android, ou `Bundle ID` no iOS)**!

## Como verificar
Dessa forma, mesmo que alguém extraia a `AIzaSy...` do APK com o MobSF ou JADX, qualquer tentativa de usá-la fora do aplicativo assinado ou para outras APIs do GCP será bloqueada pelo Google.

## Conexões
- [[mobsf-automacao-api-rest-cicd-pdf-json-scorecard-diff]] — Veja também: Automação DevSecOps com a **API REST do MobSF (`/api/v1/*`)**: Upload, Scan, Relatório JSON/PDF, **App Security Scorecard** e **Diff/Compare de Versões**.
- [[mobsf-implantacao-corporativa-autenticacao-saml-sso-postgres-seguranca]] — Veja também: Implantação Corporativa Segura do MobSF: Autenticação **SAML 2.0 SSO (`python3-saml`)**, Banco **PostgreSQL**, Filas Assíncronas (`django-q2`) e Hardening.
- [[mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx]] — Referência cruzada direta com mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx.
- [[jadx-auditoria-segredos-hardcoded-strings-xml-buildconfig-native-libs]] — Referência cruzada direta com jadx-auditoria-segredos-hardcoded-strings-xml-buildconfig-native-libs.

## Fontes
- [Mobile Security Framework (MobSF) Official GitHub — All-in-One Mobile SAST, DAST & Malware Analysis](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/README.md) — repositório oficial do MobSF cobrindo análise estática e dinâmica de pacotes Android (APK/AAB), iOS (IPA) e Windows (APPX); consultado em 2026-10-03.
- [MobSF Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/pyproject.toml) — especificação oficial dos motores integrados no MobSF 4.5+ (`libsast`, `apkid`, `apksigtool`, `lief`, `macholib`, `frida`, `http-tools`, `python3-saml`); consultado em 2026-10-03.
- [MobSF `mobsfscan` Official GitHub — Shift-Left Static Analysis CLI for Android & iOS Source Code](https://raw.githubusercontent.com/MobSF/mobsfscan/main/README.md) — documentação oficial do `mobsfscan` cobrindo análise SAST de código Java/Kotlin/Swift/ObjC e exportação SARIF/SonarQube; consultado em 2026-10-03.
