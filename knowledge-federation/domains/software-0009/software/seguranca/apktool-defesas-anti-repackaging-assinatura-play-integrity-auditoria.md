---
id: software.seguranca.tranche10.000940
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

# Engenharia Defensiva Mobile (**OWASP MASVS-RESILIENCE**): Detecção de **Repackaging (`Apktool`)**, Verificação de Certificado de Assinatura e **Play Integrity API**

## Em uma frase
Como proteger seu aplicativo Android corporativo ou financeiro contra atacantes que usam o **Apktool** para remover verificações de segurança, injetar malware/trojans bancários e redistribuir um APK adulterado (*Repackaged APK*)?

## Por que importa
A primeira camada de defesa (auditada na categoria **OWASP MASVS-RESILIENCE**) é a **Verificação de Integridade e Assinatura**: como o atacante que recompila o APK com `apktool b` não possui a chave privada original da empresa, ele é obrigado a assinar o APK modificado com uma nova chave!

## Como funciona
No entanto, fazer essa checagem apenas em Java (`PackageManager.GET_SIGNING_CERTIFICATES` comparando com uma string SHA-256 hardcoded) é facilmente contornado editando 2 linhas de `.smali` no próprio Apktool! A defesa robusta exige combinar: **(1)** verificação do hash do certificado de assinatura e do CRC do `classes.dex` dentro de código nativo C/C++ (JNI) lendo diretamente `/proc/self/maps` e o bloco APK Signature Scheme v2/v3; e **(2) Atestação Remota Criptográfica no Backend via Google Play Integrity API (`MEETS_STRONG_INTEGRITY` + `APP_RECOGNIZED`)**!

## Exemplo
```bash
# Extrair e inspecionar o hash SHA-256 do certificado de assinatura de um APK para documentar no relatorio OWASP MASVS
apksigner verify --print-certs /cases/mobile/target_app.apk | grep -E 'Signer #1 certificate (DN|SHA-256)'
```

## Limites e trade-offs
Por que a validação do token da **Google Play Integrity API no servidor backend** é o controle definitivo contra repackaging? Porque o token JWS assinado pelos servidores da Google atesta criptograficamente o hash do binário do APK (`appRecognitionVerdict`) e o certificado de assinatura: se o APK foi modificado no Apktool, o backend recusa a sessão independentemente de qualquer patch feito no cliente!

## Como verificar
Durante o pentest mobile, sempre teste se o aplicativo recompilado e re-assinado com sua chave de teste continua conseguindo autenticar nas APIs do backend.

## Conexões
- [[apktool-anatomia-apktool-yml-sdkinfo-donotcompress-unkownfiles]] — Veja também: Apktool: Anatomia do Arquivo de Controle **`apktool.yml`** (`sdkInfo`, `versionInfo`, `doNotCompress` e `unknownFiles`).
- [[apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3]] — Referência cruzada direta com apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3.
- [[apktool-engenharia-reversa-edicao-bytecode-smali-registradores-patch]] — Referência cruzada direta com apktool-engenharia-reversa-edicao-bytecode-smali-registradores-patch.

## Fontes
- [Apktool Official GitHub Repository — Reverse Engineering Android APK Resources & Smali](https://raw.githubusercontent.com/iBotPeaches/Apktool/main/README.md) — repositório oficial do Apktool cobrindo decodificação de recursos binários Android e reconstrução de pacotes APK; consultado em 2026-10-03.
- [Apktool Official Documentation — Introduction to APK Structure, AXML Decoding & Baksmali](https://apktool.org/wiki/the-basics/intro/) — documentação oficial do Apktool detalhando a decodificação de `AndroidManifest.xml`, `resources.arsc` e desmontagem `classes.dex`; consultado em 2026-10-03.
