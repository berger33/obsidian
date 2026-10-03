---
id: software.seguranca.tranche10.000933
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/iBotPeaches/Apktool/main/README.md", "https://apktool.org/wiki/the-basics/intro/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Apktool na Prática: Habilitando **Interceptação HTTPS de CAs de Usuário (`network_security_config.xml`)** e **`android:debuggable="true"`** em Android 7+

## Em uma frase
A partir do **Android 7.0 (Nougat, API 24)**, aplicativos com `targetSdkVersion >= 24` deixaram de confiar por padrão nos certificados CA instalados pelo usuário nas configurações do celular (confiando apenas nas CAs de sistema em `/system/etc/security/cacerts/`): como resultado, se você estiver testando o aplicativo em um **celular físico não-roteado**, o tráfego HTTPS será rejeitado quando passar pelo **`mitmproxy`**, **OWASP ZAP** ou **Burp Suite**!

## Por que importa
Como resolver isso em menos de 1 minuto em qualquer celular sem precisar de Root? Usando o **Apktool (`apktool d -s`)** para injetar uma **Configuração de Segurança de Rede (`res/xml/network_security_config.xml`)** que autoriza certificados de usuário (`<certificates src="user" />`) e referenciá-la no atributo **`android:networkSecurityConfig="@xml/network_security_config"`** dentro da tag `<application>` do `AndroidManifest.xml`!

## Como funciona
Na mesma edição da tag `<application>`, adicionar **`android:debuggable="true"`** habilita depuração JDWP e acesso à sandbox `/data/data/<pacote>` via `adb shell run-as <pacote>`!

## Exemplo
```xml
<!-- res/xml/network_security_config.xml — Autorizando certificados CA de usuario (mitmproxy/ZAP) para auditoria dinamica -->
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <base-config cleartextTrafficPermitted="true">
        <trust-anchors>
            <certificates src="system" />
            <certificates src="user" overridePins="true" />
        </trust-anchors>
    </base-config>
</network-security-config>
```

## Limites e trade-offs
Ao auditar um aplicativo no sentido **defensivo (Blue Team / AppSec)**, verifique sempre se o desenvolvedor não esqueceu `<certificates src="user" />` ou `<debug-overrides>` ativos no `network_security_config.xml` da build de produção publicada na Google Play Store!

## Como verificar
Depois de salvar o `network_security_config.xml` e atualizar a tag `<application>` no `AndroidManifest.xml`, recompile e assine o APK com `apktool b`, `zipalign` e `apksigner`.

## Conexões
- [[apktool-controles-decodificacao-no-src-no-res-only-main-classes]] — Veja também: Apktool (`d` / `decode`): Uso Cirúrgico de **`-s` (`--no-src`)**, **`-r` (`--no-res`)** e **`--only-main-classes`** para Evitar Erros de `aapt2` em APKs Complexos.
- [[apktool-engenharia-reversa-edicao-bytecode-smali-registradores-patch]] — Veja também: Apktool & **Bytecode Smali**: Anatomia de Métodos (`.locals`, `v0`/`p0`), Desvios Condicionais (`if-eqz`/`if-nez`) e Patching de *Root Detection* / *SSL Pinning*.
- [[apktool-arquitetura-decodificacao-resources-arsc-axml-baksmali]] — Referência cruzada direta com apktool-arquitetura-decodificacao-resources-arsc-axml-baksmali.
- [[apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3]] — Referência cruzada direta com apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3.
- [[mitmproxy-autoridade-certificadora-mitm-it-mtls-client-certs-sslkeylogfile]] — Referência cruzada direta com mitmproxy-autoridade-certificadora-mitm-it-mtls-client-certs-sslkeylogfile.

## Fontes
- [Apktool Official GitHub Repository — Reverse Engineering Android APK Resources & Smali](https://raw.githubusercontent.com/iBotPeaches/Apktool/main/README.md) — repositório oficial do Apktool cobrindo decodificação de recursos binários Android e reconstrução de pacotes APK; consultado em 2026-10-03.
- [Apktool Official Documentation — Introduction to APK Structure, AXML Decoding & Baksmali](https://apktool.org/wiki/the-basics/intro/) — documentação oficial do Apktool detalhando a decodificação de `AndroidManifest.xml`, `resources.arsc` e desmontagem `classes.dex`; consultado em 2026-10-03.
