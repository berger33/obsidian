---
id: software.seguranca.tranche11.001042
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
fontes: ["https://raw.githubusercontent.com/sensepost/objection/master/README.md", "https://github.com/sensepost/objection/wiki/Patching-Android-Applications"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Instrumentação Sem Root/Jailbreak com **`objection patchapk`** e **`objection patchipa`**: Automação do `frida-gadget` e Configurações de Script

## Em uma frase
Muitos aplicativos bancários, governamentais e corporativos possuem proteções avançadas contra Root/Jailbreak que impedem sua execução em aparelhos modificados — ou exigem recursos de hardware (como o chip **Secure Enclave / StrongBox** ou biometria real) que não existem em emuladores.

## Por que importa
Conforme documentado no guia oficial (`wiki/Patching-Android-Applications`), o comando **`objection patchapk --source app.apk`** automatiza 100% os 7 passos manuais que vimos no Apktool: **(1)** Consulta a arquitetura da CPU do celular conectado via `adb` (ou usa `--architecture arm64-v8a`); **(2)** Baixa a versão correspondente do `frida-gadget.so`; **(3)** Desempacota o APK com `apktool`; **(4)** Injeta a permissão `android.permission.INTERNET` no `AndroidManifest.xml` caso não exista; **(5)** Localiza a Activity principal e injeta a chamada Smali `invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V` para `"frida-gadget"`; **(6)** Copia a `.so` para `lib/<arch>/libfrida-gadget.so`; e **(7)** Recompila e assina o novo APK (`app.objection.apk`)!

## Como funciona
No **iOS**, o comando equivalente **`objection patchipa --source app.ipa --codesign-signature <SHA1>`** injeta o `FridaGadget.dylib` dentro do pacote `.ipa` e o reassina com seu certificado de desenvolvedor Apple!

## Exemplo
```bash
# Extrair o APK instalado de um aparelho Android sem root via adb e injetar automaticamente o Frida Gadget com objection patchapk
adb shell pm path com.empresa.mobileapp
adb pull /data/app/com.empresa.mobileapp-1/base.apk app-original.apk
objection patchapk --source app-original.apk --use-aapt2
adb install app-original.objection.apk
```

## Limites e trade-offs
E se o aplicativo no Android usar **Split APKs / App Bundles** (vários arquivos `base.apk`, `split_config.arm64_v8a.apk`, `split_config.pt.apk` retornados por `adb shell pm path`)? O `objection` também suporta o modo **`objection signapk`** para assinar todos os splits com a mesma chave após aplicar o patch no split principal!

## Como verificar
Você também pode passar `--gadget-config config.json` no `patchapk`/`patchipa` para configurar o Frida Gadget em modo `script` autônomo sem precisar conectar o computador.

## Conexões
- [[objection-arquitetura-runtime-mobile-exploration-frida-repl-usb]] — Veja também: **SensePost Objection (`sensepost/objection`)**: Arquitetura de Exploração Mobile em Runtime sobre **Frida** para **Android e iOS Sem Root/Jailbreak**.
- [[objection-bypass-ssl-pinning-android-ios-network-security-trustkit]] — Veja também: Bypass Universal de **SSL/TLS Certificate Pinning** no `objection`: **`android sslpinning disable`** e **`ios sslpinning disable`** (`OkHttp3`, `Conscrypt`, `TrustKit`, `NSURLSession`).
- [[apktool-injecao-frida-gadget-so-smali-dispositivos-sem-root]] — Referência cruzada direta com apktool-injecao-frida-gadget-so-smali-dispositivos-sem-root.

## Fontes
- [SensePost Objection Official GitHub — Runtime Mobile Exploration Toolkit Powered by Frida](https://raw.githubusercontent.com/sensepost/objection/master/README.md) — repositório oficial do `objection` cobrindo exploração em tempo de execução para Android e iOS sem necessidade de root/jailbreak; consultado em 2026-10-03.
- [SensePost Objection Official Wiki — Patching Android & iOS Applications (`patchapk` / `frida-gadget`)](https://github.com/sensepost/objection/wiki/Patching-Android-Applications) — documentação oficial detalhando o processo automatizado de injeção do `frida-gadget.so`, reempacotamento e assinatura; consultado em 2026-10-03.
