---
id: software.seguranca.tranche06.000543
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/kevoreilly/CAPEv2/master/README.md", "https://capev2.readthedocs.io/en/latest/usage/api.html", "https://github.com/CAPESandbox/CAPE-parsers"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CAPEv2 Sandbox: Programação Dinâmica do Debugger via Assinaturas **YARA** (`meta: cape_options`) para Unpacking e Anti-Sandbox

## Em uma frase
Um dos recursos mais avançados do CAPEv2 é a capacidade de **programar o debugger em tempo real durante a detonação usando regras YARA**: sempre que uma região de memória é alocada ou decifrada, o `capemon` executa um scan YARA em memória e, se uma regra casar, lê a diretiva **`cape_options`** nos metadados da regra para setar breakpoints de hardware nos offsets exatos encontrados.

## Por que importa
Em vez de escrever um desempacotador manual em C para cada variante de packer (como derivados de UPX, VMProtect ou loaders customizados), o analista escreve uma regra YARA que localiza a sequência de bytes do *tail jump* (o salto para o OEP) e instrui o debugger a pausar naquele endereço exato (`bp0=$tail_jmp`) e despejar o processo limpo.

## Como funciona
O mesmo mecanismo YARA + Debugger permite criar **contramedidas dinâmicas anti-sandbox**: se a regra YARA detectar uma rotina específica de checagem de VM ou atraso malicioso em memória, `cape_options` pode instruir o debugger a pular a instrução (`eip` / `rip` patch) ou forçar o valor de retorno do registrador.

## Exemplo
```yara
rule Custom_UPX_Variant_OEP_Dumper {
    meta:
        description = "Localiza o salto final (OEP) de variante UPX e programa breakpoint no debugger do CAPE"
        cape_options = "bp0=$oep_jump,action0=dump,type=upx"
    strings:
        $oep_jump = { 83 EC ?? E9 ?? ?? ?? ?? 00 }
    condition:
        uint16(0) == 0x5A4D and $oep_jump
}
```

## Limites e trade-offs
O debugger do CAPEv2 dispõe de 4 registradores de debug de hardware da arquitetura x86/x64 (`dr0` a `dr3`, mapeados como `bp0` a `bp3` em `cape_options`); evite definir mais de 4 breakpoints simultâneos na mesma assinatura.

## Como verificar
Adicione a regra YARA de teste no diretório de assinaturas YARA do monitor do CAPEv2, detone um binário empacotado com UPX e verifique no log do debugger o acionamento de `bp0` e o dump no OEP.

## Conexões
- [[capev2-desempacotamento-dinamico-process-injection-unpacking]] — Veja também: CAPEv2 Sandbox: Desempacotamento Dinâmico Automático (*Passive* vs *Active Unpacking* `unpacker=2`) e Captura de Injeções.
- [[capev2-extracao-configuracao-malware-cape-parsers-maco-malduck]] — Veja também: CAPEv2 Sandbox: Extração Estática e Dinâmica de Configuração de Malware (`CAPE-parsers`, `extract_config`, `MaCo` e `MalDuck`).
- [[capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara]] — Referência cruzada direta com capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara.

## Fontes
- [CAPEv2 Official GitHub — Malware Configuration And Payload Extraction](https://raw.githubusercontent.com/kevoreilly/CAPEv2/master/README.md) — documentação oficial do CAPEv2 cobrindo unpacking dinâmico, debugger programável por YARA, AMSI e CAPE-parsers; consultado em 2026-10-03.
- [CAPEv2 Official Documentation — REST API v2 Reference](https://capev2.readthedocs.io/en/latest/usage/api.html) — referência oficial da REST API v2 (/apiv2/), autenticação por token DRF, throttling e endpoints de tarefas; consultado em 2026-10-03.
- [CAPE-parsers Official Repository — Static Configuration Extractors](https://github.com/CAPESandbox/CAPE-parsers) — repositório oficial de extratores de configuração de famílias de malware do CAPEv2; consultado em 2026-10-03.
