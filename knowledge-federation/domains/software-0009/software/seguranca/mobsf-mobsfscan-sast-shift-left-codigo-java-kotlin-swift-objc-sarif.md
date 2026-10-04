---
id: software.seguranca.tranche11.001036
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

# **`mobsfscan` (`MobSF/mobsfscan`)**: SAST Shift-Left de Código-Fonte Mobile (**Java, Kotlin, Android XML, Swift, Objective-C e `Info.plist`**) com Saída **SARIF e SonarQube**

## Em uma frase
Esperar que o pacote `.apk` ou `.ipa` inteiro seja compilado para só então enviá-lo a um servidor MobSF pode demorar vários minutos em um Pull Request. E se você pudesse rodar **todas as regras de análise estática do MobSF diretamente sobre o código-fonte em poucos segundos** a cada commit do desenvolvedor?

## Por que importa
Para isso a equipe do MobSF criou o **`mobsfscan`** (`MobSF/mobsfscan`, instalável via `pip install mobsfscan`), um scanner CLI leve movido por **`libsast`** e **`semgrep`** que analisa código-fonte **Java, Kotlin, XML Android, Swift, Objective-C e `Info.plist` iOS** sem precisar compilar o aplicativo nem subir o container do MobSF!

## Como funciona
Conforme documentado no `README.md` oficial do `mobsfscan`, cada regra violada já traz mapeamento completo de **CVSS, CWE, OWASP Mobile Top 10 e OWASP MASVS / MSTG**, e suporta exportação nativa em **`--sarif` (SARIF 2.1.0 para GitHub Code Scanning)**, **`--sonarqube` (SonarQube 10.3+)**, **`--gitlab-sast`**, **`--json`** e **`--html`**!

## Exemplo
```bash
# Executar o mobsfscan sobre um repositorio mobile exportando em SARIF 2.1.0 e falhando o pipeline em caso de vulnerabilidades
pip install mobsfscan
mobsfscan . \
  --type auto \
  --sarif \
  --output mobsfscan-results.sarif \
  --exit-warning
```

## Limites e trade-offs
Para controlar falsos positivos ou ignorar pastas de testes no `mobsfscan`, crie um arquivo **`.mobsf`** (em formato YAML) na raiz do repositório definindo `ignore-filenames`, `ignore-paths`, `ignore-rules` e `severity-filter: [ERROR, WARNING]`, e passe-o com `-c .mobsf`!

## Como verificar
Integre o `mobsfscan --sarif` no GitHub Actions dos seus repositórios Android e iOS para comentar vulnerabilidades MASVS diretamente nas linhas do Pull Request.

## Conexões
- [[mobsf-instrumentacao-frida-live-api-monitor-scripts-auxiliares]] — Veja também: MobSF **Live API Monitor & Frida Code Editor**: Monitoramento de Criptografia/Rede em Tempo Real e Scripts Auxiliares (`SSL Pinning`, `Root Bypass`, `Hook`).
- [[mobsf-analise-privacidade-trackers-exodus-permissoes-malware-domains]] — Veja também: Auditoria de **Privacidade (LGPD/GDPR), Rastreadores (`Exodus Privacy`) e Inteligência de Malware** no MobSF: SDKs de Terceiros, Domínios, GeoIP e Quarks/APKiD.
- [[mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx]] — Referência cruzada direta com mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx.
- [[mobsf-automacao-api-rest-cicd-pdf-json-scorecard-diff]] — Referência cruzada direta com mobsf-automacao-api-rest-cicd-pdf-json-scorecard-diff.
- [[codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg]] — Referência cruzada direta com codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg.

## Fontes
- [Mobile Security Framework (MobSF) Official GitHub — All-in-One Mobile SAST, DAST & Malware Analysis](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/README.md) — repositório oficial do MobSF cobrindo análise estática e dinâmica de pacotes Android (APK/AAB), iOS (IPA) e Windows (APPX); consultado em 2026-10-03.
- [MobSF Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/pyproject.toml) — especificação oficial dos motores integrados no MobSF 4.5+ (`libsast`, `apkid`, `apksigtool`, `lief`, `macholib`, `frida`, `http-tools`, `python3-saml`); consultado em 2026-10-03.
- [MobSF `mobsfscan` Official GitHub — Shift-Left Static Analysis CLI for Android & iOS Source Code](https://raw.githubusercontent.com/MobSF/mobsfscan/main/README.md) — documentação oficial do `mobsfscan` cobrindo análise SAST de código Java/Kotlin/Swift/ObjC e exportação SARIF/SonarQube; consultado em 2026-10-03.
