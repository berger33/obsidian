---
id: software.seguranca.tranche11.001038
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

# Automação DevSecOps com a **API REST do MobSF (`/api/v1/*`)**: Upload, Scan, Relatório JSON/PDF, **App Security Scorecard** e **Diff/Compare de Versões**

## Em uma frase
Para transformar o MobSF em um portão de qualidade (*Security Gate*) 100% automatizado nos seus pipelines de release mobile (GitHub Actions, GitLab CI, Bitrise, Fastlane) e integrá-lo ao **OWASP DefectDojo**, você utiliza a **API REST autenticada (`/api/v1/*` via cabeçalho `Authorization: <API_KEY>`)**!

## Por que importa
Veja os 6 endpoints fundamentais da API REST do MobSF:

## Como funciona
**(1) `POST /api/v1/upload`** — envia o `.apk`/`.aab`/`.ipa`/`.zip` e retorna o `hash` MD5; **(2) `POST /api/v1/scan`** — executa a análise completa; **(3) `POST /api/v1/scorecard`** — retorna o **App Security Score (`0–100`)** e o resumo de achados `high`/`warning`/`info`; **(4) `POST /api/v1/report_json`** — retorna o JSON completo (aceito nativamente pelo importador **`MobSF Scan`** do DefectDojo!); **(5) `POST /api/v1/download_pdf`** — gera o relatório executivo em PDF; e **(6) `POST /api/v1/compare`** — compara lado a lado o `hash` da versão anterior com o `hash` da nova versão para mostrar exatamente o que mudou entre duas releases!

## Exemplo
```bash
# Comparar duas versoes de um aplicativo mobile via API REST do MobSF (/api/v1/compare) e consultar o Scorecard da nova release
MOBSF_API_KEY="sua_chave_api_mobsf_aqui"
HASH_V1="11112222333344445555666677778888"
HASH_V2="9999aaaabbbbccccddddeeeeffff0000"

curl -sS -X POST http://127.0.0.1:8000/api/v1/scorecard \
  -H "Authorization: ${MOBSF_API_KEY}" \
  -d "hash=${HASH_V2}" | jq '{security_score: .security_score, high_findings: (.high | length)}'

curl -sS -X POST http://127.0.0.1:8000/api/v1/compare \
  -H "Authorization: ${MOBSF_API_KEY}" \
  -d "hash1=${HASH_V1}&hash2=${HASH_V2}" -o /cases/mobile/diff_v1_v2.json
```

## Limites e trade-offs
O endpoint **`/api/v1/compare`** é extraordinário para revisões de release: em vez de ler um relatório de 50 páginas toda semana, o engenheiro de AppSec analisa apenas o diff entre a release da semana passada (`hash1`) e a release de hoje (`hash2`), vendo imediatamente quais novas permissões Android/iOS, novas atividades exportadas, novos SDKs trackers ou novos domínios externos foram introduzidos!

## Como verificar
Após exportar o relatório JSON para o DefectDojo, você pode limpar o binário do servidor MobSF chamando `POST /api/v1/delete_scan` com `hash=<md5>`.

## Conexões
- [[mobsf-analise-privacidade-trackers-exodus-permissoes-malware-domains]] — Veja também: Auditoria de **Privacidade (LGPD/GDPR), Rastreadores (`Exodus Privacy`) e Inteligência de Malware** no MobSF: SDKs de Terceiros, Domínios, GeoIP e Quarks/APKiD.
- [[mobsf-auditoria-segredos-entropia-firebase-aws-google-services-json]] — Veja também: Caça a Credenciais Cloud e **Bancos Firebase Abertos (`google-services.json` / `GoogleService-Info.plist`)** em Aplicativos Mobile com MobSF.
- [[mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx]] — Referência cruzada direta com mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx.
- [[mobsf-mobsfscan-sast-shift-left-codigo-java-kotlin-swift-objc-sarif]] — Referência cruzada direta com mobsf-mobsfscan-sast-shift-left-codigo-java-kotlin-swift-objc-sarif.

## Fontes
- [Mobile Security Framework (MobSF) Official GitHub — All-in-One Mobile SAST, DAST & Malware Analysis](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/README.md) — repositório oficial do MobSF cobrindo análise estática e dinâmica de pacotes Android (APK/AAB), iOS (IPA) e Windows (APPX); consultado em 2026-10-03.
- [MobSF Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/pyproject.toml) — especificação oficial dos motores integrados no MobSF 4.5+ (`libsast`, `apkid`, `apksigtool`, `lief`, `macholib`, `frida`, `http-tools`, `python3-saml`); consultado em 2026-10-03.
- [MobSF `mobsfscan` Official GitHub — Shift-Left Static Analysis CLI for Android & iOS Source Code](https://raw.githubusercontent.com/MobSF/mobsfscan/main/README.md) — documentação oficial do `mobsfscan` cobrindo análise SAST de código Java/Kotlin/Swift/ObjC e exportação SARIF/SonarQube; consultado em 2026-10-03.
