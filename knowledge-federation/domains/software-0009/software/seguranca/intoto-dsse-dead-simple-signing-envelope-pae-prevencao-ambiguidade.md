---
id: software.seguranca.tranche03.000257
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/in-toto/attestation/main/README.md", "https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md", "https://github.com/in-toto/attestation"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# in-toto Envelope de Assinatura `DSSE` (*Dead Simple Signing Envelope*) e `PAE`: proteção contra ataques de confusão de parser e tipo

## Em uma frase
O in-toto utiliza o **DSSE (*Dead Simple Signing Envelope*)** como camada de assinatura criptográfica para metadados `.link`, layouts e Statements de Attestation, estruturando o objeto assinado em apenas três campos (`payload` em Base64, `payloadType` como MIME/URI e `signatures` contendo `keyid` e `sig`) e assinando a codificação canônica **PAE (*Pre-Authentication Encoding*)**.

## Por que importa
Em formatos antigos de assinatura JSON (como JWS com cabeçalhos complexos mutáveis), o verificador precisava fazer parsing de estruturas JSON aninhadas ou normalizar espaços em branco (*canonicalization*) **antes** de verificar a assinatura, abrindo brechas para vulnerabilidades no próprio parser JSON.

## Como funciona
No DSSE com **PAE** (`"DSSEv1" + SP + LEN(payloadType) + SP + payloadType + SP + LEN(payload) + SP + payload`), o verificador valida a assinatura criptográfica sobre os bytes exatos **antes de decodificar o JSON**, e inclui o `payloadType` dentro da assinatura para impedir que um atacante reutilize a assinatura de um tipo de documento como se fosse outro!

## Exemplo
```json
{
  "payloadType": "application/vnd.in-toto+json",
  "payload": "eyJfdHlwZSI6Imh0dHBzOi8vaW4tdG90by5pby9TdGF0ZW1lbnQvdjEi...",
  "signatures": [
    {
      "keyid": "776a00e29f3559e0141b3b096f6966968c326e41...",
      "sig": "MEUCIQDKs8..."
    }
  ]
}
```

## Limites e trade-offs
Ao implementar um consumidor de atestados DSSE, sempre verifique a assinatura PAE e valide que `payloadType == "application/vnd.in-toto+json"` **antes** de chamar `json.Unmarshal` sobre o conteúdo decodificado de `payload`!

## Como verificar
Use `in-toto-sign --verify` para validar envelopes DSSE assinados localmente.

## Conexões
- [[intoto-predicates-catalogo-slsa-provenance-cyclonedx-spdx-vuln-vsa]] — Veja também: in-toto Attestation Predicates: catálogo oficial de predicados (`SLSA Provenance`, `SPDX`/`CycloneDX SBOM`, `Vuln Scan`, `VSA` e `Test Result`).
- [[intoto-sign-assinatura-multiplas-chaves-thresholds-gpg-ssh-ed25519]] — Veja também: in-toto Assinaturas e Quorum (`in-toto-sign` e `threshold`): exigência de múltiplas assinaturas independentes em `Layout` e `Steps`.

## Fontes
- [CNCF in-toto GitHub — README.md (Supply Chain Layout, Functionaries, Artifact Rules, in-toto-run, in-toto-record, Inspections & in-toto-verify)](https://raw.githubusercontent.com/in-toto/attestation/main/README.md) — README oficial do in-toto/in-toto documentando a estrutura de layouts, regras de encadeamento de materials/products, geração de links e verificação final; consultado em 2026-10-03.
- [CNCF in-toto Attestation Framework GitHub — README.md (Statement v1 Specification, Vetted Predicates, DSSE, SLSA Intersection & Language Bindings)](https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md) — README oficial do in-toto/attestation descrevendo a especificação do Attestation Framework v1, catálogo de predicados, definições Protobuf e interseção com SLSA; consultado em 2026-10-03.
- [CNCF in-toto — Official GitHub Repository](https://github.com/in-toto/attestation) — Repositório oficial Apache-2.0 do CNCF in-toto; consultado em 2026-10-03.
